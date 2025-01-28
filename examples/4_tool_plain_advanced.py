from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


class CityLocation(BaseModel):
    city: str
    country: str


class Olympic(BaseModel):
    year: int
    location: CityLocation


# userが言及しているオリンピックの前のオリンピックを推測する
background = "Guess the year of the Olympics that is prior to the one mentioned by the user in the context"
agent = Agent("openai:gpt-4o", result_type=Olympic, system_prompt=background)


@agent.tool_plain
def calculate_previous_olympic_year(implied_year: int) -> int:
    """Calculate the year of the previous olympics held from the context"""
    # implied_yearは、Agentが推測した「userが言及しているオリンピックの年」
    return implied_year - 4


prompt = "I saw the Rio de Janeiro Olympics last year"  # 2016
result = agent.run_sync(prompt)
print(result.data)

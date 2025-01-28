import random
from pydantic import BaseModel
from pydantic_ai import Agent


class CityLocation(BaseModel):
    city: str
    country: str


class Olympic(BaseModel):
    year: int
    location: CityLocation
    dominant_country: str


agent = Agent("openai:gpt-4o", result_type=Olympic)


@agent.tool_plain
def decide_held_year() -> int:
    """Decide the year of the olympics held"""
    years = [2012, 2016, 2020, 2024]
    return random.choice(years)


result = agent.run_sync("show me the olympics year and location")
print(result.data)

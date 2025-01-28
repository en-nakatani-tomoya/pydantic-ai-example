from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


class CityLocation(BaseModel):
    city: str
    country: str


class Olympic(BaseModel):
    year: int
    location: CityLocation


agent = Agent("openai:gpt-4o", result_type=Olympic)


@agent.tool
def decide_held_year(ctx: RunContext[str]) -> int:
    """Extract the year of the olympics held from the context"""
    return ctx.deps


prompt = "2025 this year, I wanna know about latest olympics"
result = agent.run_sync(prompt)
print(result.data)

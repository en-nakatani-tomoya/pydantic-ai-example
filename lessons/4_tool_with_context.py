from pydantic import BaseModel
from pydantic_ai import Agent, RunContext


class CityLocation(BaseModel):
    city: str
    country: str


class Olympic(BaseModel):
    year: int
    location: CityLocation
    dominant_country: str


agent = Agent("openai:gpt-4o", result_type=Olympic)


@agent.tool
def decide_held_year(ctx: RunContext[str]) -> int:
    """Extract the year of the olympics held from the context"""
    return ctx.deps


result = agent.run_sync("show me the olympics year and location", deps="I wanna know about 2024 olympics")
print(result.data)

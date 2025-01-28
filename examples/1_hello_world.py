from pydantic_ai import Agent


agent = Agent("openai:gpt-4o")

result = agent.run_sync("What is [Hello World] in French?")
print(result.data)

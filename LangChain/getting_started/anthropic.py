from langchain_anthropic import ChatAnthropic


agent = ChatAnthropic(
    model = "claude-sonnet-4-5-20250929"
)

result = agent.invoke("What is the capital of France?")
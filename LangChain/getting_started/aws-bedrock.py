from langchain_aws import ChatBedrockConverse


agent = ChatBedrockConverse(
    model = "us.amazon.nova-2-lite-v1:0"
)


response = agent.invoke("What is the capital of France?")

print(response.text)
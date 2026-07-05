from langchain_aws import ChatBedrockConverse
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatBedrockConverse(
    model = 'us.anthropic.claude-sonnet-4-5-20250929-v1:0',
    api_key = os.getenv('AWS_BEARER_TOKEN_BEDROCK'),
    region_name='us-west-1'
)

response = llm.invoke("What is capital of France?")

print(response)
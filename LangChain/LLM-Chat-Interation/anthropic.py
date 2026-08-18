from anthropic import Anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = Anthropic(
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "What is the capital of France?"
    }],
    model = "claude-opus-5"
)

for content in message:
    if content.type == "text":
        print(content.text)
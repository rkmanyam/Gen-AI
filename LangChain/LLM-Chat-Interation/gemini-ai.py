from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

interaction = client.interactions.create(
    model   = "gemini-3.5-flash-lite",
    input   = "What is capital of France?"
)

print(interaction.output_text)



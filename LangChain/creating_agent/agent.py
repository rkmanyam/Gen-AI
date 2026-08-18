from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain.agents import create_agent

load_dotenv()

@tool()
def add(a: int|float, b: int|float) -> int|float:
    """
    This tool adds two numbers
    
    Args:
        a(int|float): number
        b(int|float): number

    Returns:
    int|float: Sum of two numbers

    """
    return a + b


@tool()
def subtract(a: int|float, b: int|float) -> int|float:
    """
    This tool subtracts two numbers
    
    Args:
        a(int|float): number
        b(int|float): number

    Returns:
    int|float: Difference of two numbers

    """
    return a - b


def main():

    model = ChatGoogleGenerativeAI(
        model = "gemini-3.5-flash-lite"
    )

    agent = create_agent(
        model= model,
        tools = [ add, subtract ]
    )

    result = agent.invoke({
        "messages": [{
            "role": "user",
            "content": "What is 5 plus 3?"
        }]

    })

    for message in result['messages']:
        print(message.text)

if __name__ == "__main__":
    main()
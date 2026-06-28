@tool()
def add(a: int|float, b: int|float) -> int|float:
    """Adds two numbers together.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Sum of two numbers

    Examples:
        >>> add(2, 3)
        5
    """
    return a + b

@tool()
def subtract(a: int|float, b: int|float) -> int|float:
    """Subtracts b from a.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Difference of two numbers

    Examples:
        >>> subtract(5, 3)
        2
    """
    return a - b


@tool()
def multiply(a: int|float, b: int|float) -> int|float:
    """Multiplies two numbers together.

    Args:
        a (int | float): number
        b (int | float): number

    Returns:
        int|float: Product of two numbers

    Examples:
        >>> multiply(4, 3)
        12
    """
    return a * b


@tool()
def divide(a: int|float, b: int|float) -> float:
    """Divides a by b.

    Args:
        a (int | float): numerator
        b (int | float): denominator (must not be zero)

    Returns:
        float: Quotient of a divided by b

    Examples:
        >>> divide(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@tool()
def modulus(a: int|float, b: int|float) -> int|float:
    """Returns the remainder of a divided by b.

    Args:
        a (int | float): dividend
        b (int | float): divisor (must not be zero)

    Returns:
        int|float: Remainder of a divided by b

    Examples:
        >>> modulus(10, 3)
        1
    """
    if b == 0:
        raise ValueError("Cannot perform modulus with zero divisor")
    return a % b


def main():
    model = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        project=os.getenv('PROJECT_ID')
    )
    # result = model.invoke("What is capital of France")
    # result.pretty_print()
    agent = create_agent(
        model=model,
        tools=[add, subtract, multiply, divide, modulus],
    )
    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "What is 5 plus 3?"
            }
        ]
    })
    for message in result['messages']:
        message.pretty_print()



if __name__ == "__main__":
    main()
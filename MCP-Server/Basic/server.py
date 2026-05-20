from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="GreetMCP")

@mcp.tool(name="Hello", description="Say Hello")
def hello(name: str) -> str:
    return f"Hello {name}!"

@mcp.tool(name="Bye", description="Say Bye")
def bye(name: str) -> str:
    return f"Bye {name}!"


def main():
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
from mcp.server.fastmcp import FastMCP
import os
import debugpy

mcp = FastMCP("library-mcp-server")


@mcp.tool("add_book")
def add_book(author: str, title: str, year: str) ->str:
    return f"The book {title} written by {author} ({year}) added"


def main():
    mcp.run(transport="stdio")




if __name__ == "__main__":
    # debugpy.listen(5678)
    # print("Waiting", flush=True)
    # debugpy.wait_for_client()
    main()

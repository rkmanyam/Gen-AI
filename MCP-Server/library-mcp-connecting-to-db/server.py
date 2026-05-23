

from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import db


mcp = FastMCP("library-mcp", host="0.0.0.0", port=9000)

@mcp.tool(name="add_book")
def add_book(
    book_id: str,
    title: str,
    author: str,
    isbn: str,
    genre: str,
    available_copies: int
) -> str:
    message = db.add_book(book_id, title, author,isbn,genre,available_copies)
    return message

if __name__ == "__main__":
    mcp.run(transport="streamable-http")



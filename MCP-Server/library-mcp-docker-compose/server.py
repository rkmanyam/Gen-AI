import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import operations
from typing import Any

load_dotenv()

mcp = FastMCP(name="library-mcp", host="0.0.0.0", port="9000")


@mcp.tool(name="issue_book")
def issue_book(issued_by_librarian_id: int, student_id: int, book_id: int, date: str, status: str = 'AVAILABLE', issue_condition: str = "Good", transaction_type: str ="ISSUED", quantity: int =1) -> str:
    result = operations.issue_book(issued_by_librarian_id, student_id, book_id, date, status, issue_condition, transaction_type, quantity)
    return result


if __name__ == "__main__":
    mcp.run(transport="streamable-http")


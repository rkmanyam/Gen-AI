from fastmcp import Client
import asyncio


async def main():
    async with Client("http://localhost:9000/mcp") as client:
        tools = await client.list_tools()
        


        result = await client.call_tool(
            "add_book",
            {
                "book_id": "302",
                "title": "Book 302",
                "author": "Rk",
                "isbn": "302 Book",
                "genre": "Test",
                "available_copies": 10
            }
        )

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
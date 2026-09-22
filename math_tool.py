import os
from mcp.server.fastmcp import FastMCP

server = FastMCP("math-mcp")

@server.tool()
def add(a: float, b: float) -> float:
    """Add two numbers together."""
    return a + b


@server.tool()
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@server.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together."""
    return a * b


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    server.run(transport="streamable-http", port=port)

"""
import os
import uvicorn
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))

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
    uvicorn.run(
        server.streamable_http_app(),
        host="0.0.0.0",
        port=port,
    )
"""
import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

port = int(os.environ.get("PORT", 8000))

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
    security = TransportSecuritySettings(enable_dns_rebinding_protection=False)
    app = server.streamable_http_app(transport_security=security)
    uvicorn.run(app, host="0.0.0.0", port=port)


import os
import requests
import uvicorn
from mcp.server.fastmcp import FastMCP

port = int(os.environ.get("PORT", 8000))

server = FastMCP(
    "WhatsApp MCP Server",
    host="0.0.0.0",
    port=port
)


@server.tool()
def send_whatsapp_message(phone: str, message: str) -> str:
    """Send a WhatsApp message using the Go WhatsMeow server."""

    try:
        response = requests.post(
            "https://go-whatsapp-ivv8.onrender.com/send",
            json={
                "phone": phone,
                "message": message
            },
            timeout=30
        )

        if response.status_code == 200:
            return "Message sent successfully"

        return f"Failed to send message: {response.text}"

    except requests.RequestException as e:
        return f"Connection error: {e}"


if __name__ == "__main__":
    uvicorn.run(
        server.streamable_http_app(),
        host="0.0.0.0",
        port=port
    )

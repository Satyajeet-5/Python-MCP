import os
import uvicorn
from mcp.server.fastmcp import FastMCP
from twilio.rest import Client

account_sid = "ACfa14f3d14cc6f31423a666eb9baf2abb"
auth_token = "5579de33a27c887e614e7b24648ce2c0"
client = Client(account_sid, auth_token)

port = int(os.environ.get("PORT", 8000))

server = FastMCP("mcp-tool", host="0.0.0.0", port=port)

@server.tool()
def send_whatsapp_message(receiver: int, body: str) -> str :
    """Send WhatsApp Message from Sender to Receiver """

    message = client.messages.create(
         from_= f"whatsapp:+14155238886",
         to= f"whatsapp:+91{receiver}",
         body=body
    )

    print(message.sid)
    return message.sid
    
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
    uvicorn.run(server.streamable_http_app(), host="0.0.0.0", port=port)

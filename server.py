from mcp.server.fastmcp import FastMCP

mcp = FastMCP("serverHTTP", host="0.0.0.0", port=8000)

@mcp.tool()
def greeting(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
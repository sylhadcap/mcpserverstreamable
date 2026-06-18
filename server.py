from mcp.server.fastmcp import FastMCP

mcp = FastMCP("serverHTTP")

@mcp.tool()
def greeting(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
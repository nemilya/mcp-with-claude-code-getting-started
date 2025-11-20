from fastmcp import FastMCP

mcp = FastMCP("my-library-server")

@mcp.tool()
def process_text(text: str) -> dict:
    """Process text"""
    return {
        "original": text,
        "uppercase": text.upper(),
        "length": len(text)
    }

def main():
    mcp.run()

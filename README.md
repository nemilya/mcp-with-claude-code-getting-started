# MCP Getting Started Demo

This is a comprehensive demo project that demonstrates how to create and use MCP (Model Context Protocol) servers with Claude Code. The project shows the complete workflow from server implementation to integration with Claude Code.

## Quick Start

1. **Clone and setup the MCP server**
2. **Navigate to the app directory and start Claude Code**
3. **Use your custom MCP tools directly in Claude Code**

```bash
# 1. Setup the server
cd my-library-mcp
uv sync
uv pip install -e .

# 2. Go to app directory and start Claude Code
cd ../app-dir
claude-code

# 3. Test your MCP server in Claude Code
> /mcp list  # Should show "my-library" server
> Please process the text "Hello MCP World"
```

## Project Structure

```
mcp-with-claude-code-getting-started/
├── README.md                    # This file - main project documentation
├── my-library-mcp/              # MCP Server implementation
│   ├── my_library/
│   │   └── server.py           # Main MCP server code
│   ├── pyproject.toml          # Python project configuration
│   └── README.md               # Server-specific documentation
└── app-dir/                    # Application directory for Claude Code
    ├── .mcp.json               # MCP server configuration for Claude Code
    └── .gitignore
```

## How It Works

### 1. The MCP Server (`my-library-mcp/`)

This directory contains a fully functional MCP server built with FastMCP that provides text processing capabilities:

- **Server Name**: `my-library-server`
- **Available Tool**: `process_text(text: str)` - Processes text and returns original, uppercase version, and length
- **Framework**: FastMCP (Python)
- **Transport**: STDIO

### 2. The Application Directory (`app-dir/`)

This is where you'll run Claude Code. The key file is `.mcp.json` which tells Claude Code which MCP servers to connect to:

```json
{
  "mcpServers": {
    "my-library": {
      "command": "uv",
      "args": [
        "run",
        "--project", "../my-library-mcp",
        "my-library-mcp"
      ],
      "type": "stdio",
      "env": {
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

**Key Points**:
- The path `../my-library-mcp` is relative to the `app-dir/`
- Claude Code automatically detects and starts MCP servers defined in `.mcp.json`
- The server runs via `uv run` for proper dependency management

## Step-by-Step Setup Guide

### Prerequisites

- **Python 3.10+**
- **uv** (Python package manager) - [Install uv](https://docs.astral.sh/uv/)
- **Claude Code** - [Install Claude Code](https://claude.com/claude-code)

### Step 1: Setup the MCP Server

```bash
# Navigate to the server directory
cd my-library-mcp

# Install dependencies
uv sync

# Install the package in development mode (required!)
uv pip install -e .
```

### Step 2: Verify Server Installation

```bash
# Test that the server runs correctly
uv run my-library-mcp
```

You should see the FastMCP banner indicating the server is running.

### Step 3: Start Using with Claude Code

```bash
# Navigate to the app directory
cd ../app-dir

# Start Claude Code
claude-code
```

## Using Your MCP Server in Claude Code

Once Claude Code is running in the `app-dir/`, you can:

### Check Connected MCP Servers

```bash
> /mcp list
```

You should see:
```
Connected MCP Servers:
- my-library (my-library-server)
```

### Use Your Custom Tool

Simply ask Claude to use your tool:

```
> Please process the text "Hello World" using the process_text tool
```

Claude will respond with something like:
```
I'll process that text for you using the process_text tool.

Result:
- Original text: "Hello World"
- Uppercase: "HELLO WORLD"
- Length: 11 characters
```

## Understanding the Configuration

### The `.mcp.json` File Explained

```json
{
  "mcpServers": {
    "my-library": {                    // Server name for reference
      "command": "uv",                 // Command to run the server
      "args": [                        // Arguments for the command
        "run",
        "--project", "../my-library-mcp",  // Path to server project
        "my-library-mcp"               // Package name to run
      ],
      "type": "stdio",                 // Communication type
      "env": {                         // Environment variables
        "PYTHONUNBUFFERED": "1"        // Ensures proper Python output buffering
      }
    }
  }
}
```

### How Claude Code Uses This Configuration

1. **Auto-detection**: Claude Code automatically reads `.mcp.json` when starting
2. **Server Startup**: Claude Code launches each configured server as a subprocess
3. **Tool Registration**: The MCP server's tools become available to Claude
4. **Communication**: Claude communicates with servers using the MCP protocol via STDIO

## Extending This Demo

### Adding New Tools

1. Edit `my-library-mcp/my_library/server.py`
2. Add new functions with the `@mcp.tool()` decorator
3. Restart Claude Code to pick up the new tools

### Example: Adding a New Tool

```python
@mcp.tool()
def reverse_text(text: str) -> dict:
    """Reverse the input text and return statistics."""
    reversed_text = text[::-1]
    return {
        "original": text,
        "reversed": reversed_text,
        "length": len(text)
    }
```

### Adding Multiple Servers

You can add multiple MCP servers to your `.mcp.json`:

```json
{
  "mcpServers": {
    "my-library": {
      "command": "uv",
      "args": ["run", "--project", "../my-library-mcp", "my-library-mcp"],
      "type": "stdio"
    },
    "another-server": {
      "command": "node",
      "args": ["../another-server/index.js"],
      "type": "stdio"
    }
  }
}
```

## Troubleshooting

### Common Issues

1. **"No such file or directory" error**
   - Make sure you ran `uv pip install -e .` in the server directory
   - Verify the path in `.mcp.json` is correct

2. **Server not showing up in `/mcp list`**
   - Check that `.mcp.json` is in the same directory where you run `claude-code`
   - Verify JSON syntax is correct
   - Check server logs for startup errors

3. **Python environment issues**
   - Ensure you're using the correct Python version (3.10+)
   - Make sure uv is installed and working

### Verification Commands

```bash
# Check if server package is installed
cd my-library-mcp
uv pip list | grep my-library-mcp

# Test server directly
uv run my-library-mcp

# Check Claude Code MCP connection
cd ../app-dir
claude-code
> /mcp list
```

## Learning Resources

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [FastMCP Framework](https://github.com/jlowin/fastmcp)
- [Claude Code Documentation](https://claude.com/claude-code)
- [uv Package Manager](https://docs.astral.sh/uv/)

## Contributing

This is a demo project. Feel to experiment with:
- Adding new tools to the MCP server
- Trying different server configurations
- Exploring advanced MCP features

## License

MIT License - feel free to use this as a foundation for your own MCP projects.

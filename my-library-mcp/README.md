# My Library MCP Server

A simple MCP (Model Context Protocol) server built with FastMCP for text processing.

## Features

- **process_text**: Processes text and returns the original, uppercase version, and string length

## Installation and Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd my-library-mcp
```

### 2. Install dependencies

Make sure you have [uv](https://docs.astral.sh/uv/) installed:

```bash
# Install dependencies
uv sync

# Install package in development mode (required!)
uv pip install -e .
```

### 3. Start the server (verify)

```bash
uv run my-library-mcp
```

After starting, you'll see:
```
╭──────────────────────────────────────────────────────────────────────────────╮
│                                                                              │
│                         ▄▀▀ ▄▀█ █▀▀ ▀█▀ █▀▄▀█ █▀▀ █▀█                        │
│                         █▀  █▀█ ▄▄█  █  █ ▀ █ █▄▄ █▀▀                        │
│                                                                              │
│                                FastMCP 2.13.1                                │
│                                                                              │
│                    🖥  Server name: my-library-server                         │
│                    📦 Transport:   STDIO                                     │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Usage with Claude Desktop

Add the following configuration to your `claude_desktop_config.json` file:

```json
{
  "mcpServers": {
    "my-library": {
      "command": "uv",
      "args": ["run", "my-library-mcp"],
      "cwd": "/path/to/my-library-mcp"
    }
  }
}
```

Replace `/path/to/my-library-mcp` with the absolute path to your project.

## Available Tools

### process_text

Processes a text string and returns:
- Original text
- Uppercase text
- String length

**Parameters:**
- `text` (string): Text to process

**Usage example:**
```
Please process the text "Hello World" using the process_text tool
```

## Project Structure

```
my-library-mcp/
├── my_library/
│   └── server.py          # Main MCP server file
├── pyproject.toml         # Project configuration and dependencies
├── uv.lock               # Dependencies lock file
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## Requirements

- Python 3.10+
- uv (Python package manager)
- FastMCP 0.1.0+

## Troubleshooting

### "No such file or directory (os error 2)" Error

If you see this error when running `uv run my-library-mcp`, make sure you installed the package in development mode:

```bash
uv pip install -e .
```

This needs to be done once after cloning the project or changing dependencies.

### Installation verification

To verify the package is installed correctly:

```bash
uv pip list | grep my-library-mcp
```

You should see something like:
```
my-library-mcp      0.1.0        /path/to/your/project
```

## License

MIT License

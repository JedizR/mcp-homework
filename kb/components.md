# Components

Three components.

- **MCP server** — exposes tools to Claude over the Model Context Protocol; built with FastMCP
- **Memory store** — a local JSON file holding all named memories with timestamps and tags
- **Query layer** — handles lookups by name or tag and returns matches to the caller

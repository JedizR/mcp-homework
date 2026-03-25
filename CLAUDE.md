# Project rules

- Python 3.11+, type hints on every function signature
- One function, one responsibility
- Docstrings required — they become MCP tool descriptions, so write them precisely
- No hardcoded secrets, no bare `except`, no `print()` in library code
- Conventional commits: `type(scope): imperative subject` — e.g. `feat(server): add verb replacement tool`

## Why these rules

A small MCP server has almost no room for ambiguity. Type hints aren't optional here — FastMCP reads them directly to build the tool schema, so a missing hint silently breaks your tool's description. One function, one job, because when something fails at 2am you want to know exactly where to look. Conventional commits are free documentation; future-you will thank present-you. The no-secrets and no-bare-except rules exist because that class of bug fails quietly and takes forever to find.

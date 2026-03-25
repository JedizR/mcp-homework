# Architecture

## Data flow

```
+--------+     MCP protocol      +-----------+     read/write     +------------+
| Claude | --------------------> | MCP server| -----------------> | memory.json|
|        | <--------------------  |           | <----------------- |            |
+--------+     tool result       +-----------+                    +------------+
```

Claude calls a tool over MCP. The server receives it, reads or writes the local JSON file, and returns a result. The whole thing is synchronous and local — one process, one file.

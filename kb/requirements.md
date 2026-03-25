# Requirements

## Functional

1. Store a memory given a name, body, and optional tags
2. Retrieve memories by name or tag
3. Update an existing memory by name
4. Delete a memory by name
5. Return a clear error when a requested memory doesn't exist

## Non-functional

- Reads complete in under 100ms on local storage
- No data leaves the machine
- The memory store is plain JSON — readable with any text editor, no special tooling required

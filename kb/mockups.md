# Mockups

## Storing a memory

User says to Claude: "Remember that I prefer dark mode in all my projects."

Claude calls `store_memory` with:
- name: "ui-preference-dark-mode"
- body: "User prefers dark mode in all projects"
- tags: ["ui", "preferences"]

Server writes the entry to memory.json and returns: "Stored."

---

## Retrieving a memory

User asks Claude: "What do you know about my UI preferences?"

Claude calls `get_memory` with:
- query: "ui"

Server finds the entry tagged "ui" and returns the body. Claude reads it and answers the user directly.

import nltk
from fastmcp import FastMCP

mcp = FastMCP("VerbJedi")


def _replace_verbs(sentence: str, replacement: str) -> str:
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    return " ".join(replacement if tag.startswith("VB") else word for word, tag in tags)


@mcp.tool()
def verbify_jedi(sentence: str) -> str:
    """Replace every verb in the sentence with the word Jedi. Uses NLTK POS tags."""
    if not sentence.strip():
        raise ValueError("sentence must be non-empty")
    return _replace_verbs(sentence, "Jedi")


@mcp.tool()
def verbify_keyword(sentence: str, keyword: str) -> str:
    """Replace every verb in the sentence with a user-supplied keyword. Uses NLTK POS tags."""
    if not sentence.strip():
        raise ValueError("sentence must be non-empty")
    if not keyword.strip():
        raise ValueError("keyword must be non-empty")
    return _replace_verbs(sentence, keyword)


if __name__ == "__main__":
    mcp.run()

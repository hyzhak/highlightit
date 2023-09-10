import re
from IPython.display import Markdown


def highlight(text: str, pattern: str, flags=re.IGNORECASE) -> Markdown:
    # Highlight matched substrings
    highlighted_text = re.sub(pattern, r'<mark>\g<0></mark>', text, flags=flags)

    # Display as Markdown
    return Markdown(highlighted_text)

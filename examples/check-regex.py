import re

data = """
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C --|One| --> D[Laptop]
    C --|Two|--> E[iPhone]
    C -->|Three| F[fa:fa-car Car]
"""

regex = r"([A-Za-z0-9]+)\s*-->\s*(?:\|([^|]+)\|\s*)?([A-Za-z0-9]+)"
matches = re.findall(regex, data)

for match in matches:
    parent_id, label, child_id = match
    label = label if label else None
    print(f"Parent: {parent_id}, Label: {label}, Child: {child_id}")

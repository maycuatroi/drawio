from drawio.itergrations.mermaid.mermaid_controller import MermaidController

mermaid_text = """flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]"""


def mermaid_to_drawio(mermaid_text):
    mermaid_controller = MermaidController()
    graph = mermaid_controller.load(mermaid_text)
    drawio_file = graph.render(file_name="sample.drawio", show=False)
    print(f"Exported to {drawio_file}")


if __name__ == "__main__":
    mermaid_to_drawio(mermaid_text)

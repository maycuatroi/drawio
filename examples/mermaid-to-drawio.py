from drawio.itergrations.mermaid.mermaid_controller import MermaidController

mermaid_text = """flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]"""

mermaid_controller = MermaidController()
graph = mermaid_controller.load(mermaid_text)
df_file = graph.render(file_name="sample.pdf", show=True)

import pytest

from drawio.itergrations.mermaid.mermaid_controller import MermaidController


def mermaid_to_drawio(mermaid_text):
    mermaid_controller = MermaidController()
    graph = mermaid_controller.load(mermaid_text)
    # drawio_file = graph.render(file_name="sample.drawio", show=False)
    print('Success building graph')


def test_mermaid_to_drawio_empty_input():
    mermaid_text = ""
    with pytest.raises(Exception):
        mermaid_to_drawio(mermaid_text)


def test_mermaid_to_drawio_valid_input():
    mermaid_text = """
    flowchart TD
    A[Christmas] -->|Get money| B((Go shopping))
    B --> C{Let me think}
    C --> D[Laptop]
    C --|Two|--> E[iPhone]
    C -->|Three| F[fa:fa-car Car]
    """
    mermaid_to_drawio(mermaid_text)


def test_mermaid_to_drawio_incorrect_input():
    mermaid_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit
    """
    with pytest.raises(Exception):
        mermaid_to_drawio(mermaid_text)


def test_mermaid_to_drawio_non_string_input():
    mermaid_text = 12345
    with pytest.raises(Exception):
        mermaid_to_drawio(mermaid_text)

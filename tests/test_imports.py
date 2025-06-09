from drawio import Graph, Node


def test_public_imports():
    graph = Graph()
    node = Node("A")
    graph.add_node(node)
    assert node in graph.nodes

from drawio.entities.graph.graph import Graph
from drawio.entities.graph.node import Node


def test_graph():
    node_a = Node("Christmas", shape="rectangle")
    node_b = Node("Go shopping", shape="rectangle")
    node_c = Node("Let me think", shape="oval")
    node_d = Node("Laptop", shape="rectangle")
    node_e = Node("iPhone", shape="rectangle")
    node_f = Node("Car", shape="rectangle")

    graph = Graph()
    graph.add_nodes([node_a, node_b, node_c, node_d, node_e, node_f])
    node_a >> "Get money" >> node_b
    node_b >> node_c >> "One" >> node_d
    node_c >> "Two" >> node_e
    node_c >> "Three" >> node_f

    graph.to_draw_io_csv()

from drawio import Graph, Node

node_tessa_miller = Node("Tessa Miller", shape="rectangle")


graph_config = GraphConfig()

graph = Graph()
graph.set_label("Tessa Miller")
graph.add_nodes([node_tessa_miller])

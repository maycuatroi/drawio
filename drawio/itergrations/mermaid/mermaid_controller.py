import re

from drawio.entities.base_entity import BaseEntity
from drawio.entities.graph.graph import Graph
from drawio.entities.graph.node import Node


class MermaidController(BaseEntity):
    valid_graph_types = ["flowchart"]

    def __init__(self):
        super().__init__()
        self.__data = ""
        self.__graph_type = None

    def load(self, data: str) -> "Graph":
        """Load mermaid data from a string."""
        self.__data = data.strip()
        self.__get_graph_type()

        graph = self.__build_flow_chart()
        return graph

    def __get_graph_type(self):
        """Get the graph type from the mermaid data."""
        first_line = self.__data.split("\n")[0]
        self.__graph_type = first_line.split(" ")[0].lower()
        if self.__graph_type not in self.valid_graph_types:
            raise NotImplementedError(
                f"Graph type '{self.__graph_type}' is not supported."
            )
        return self.__graph_type

    def __build_flow_chart(self) -> "Graph":
        """Build a graph from a mermaid flowchart.
        Example:
            flowchart TD
                A[Christmas] -->|Get money| B(Go shopping)
                B --> C{Let me think}
                C --|One| --> D[Laptop]
                C --|Two|--> E[iPhone]
                C -->|Three| F[fa:fa-car Car]
        """
        graph = Graph(graph_type=self.__graph_type)
        # get nodes using regex
        regex = r"(\w+)\s*(\[.*?\]|\(.*?\)|\{.*?\})"
        matches = re.findall(regex, self.__data)
        for match in matches:
            if match[0]:
                node_id = match[0]
                node_label = match[1]
            else:
                node_id = match[2]
                node_label = match[4]
            # extract node shape from label
            node_shape, node_label = self.__extract_node_shape(node_label)
            node = Node(id=node_id, name=node_label, shape=node_shape)
            graph.add_node(node)

        # simple data
        normalized_data = self.__data

        for node in graph.nodes:
            # remove node_name and keep only node id in data
            normalized_data = normalized_data.replace(node.name, "")
            # remove all open and close brackets
            # Brackes: (, ), [, ], {, }, ((, )), [[, ]], {{, }}, (((, ))), [[[, ]]], {{{, }}}, [(, )],
            regex = r"(\(|\)|\[|\]|\{|\}|\(\(|\)\)|\[\[|\]\]|\{\{|\}\}|\(\(\(|\)\)\)|\[\[\[|\]\]\]|\{\{\{|\}\}\}|\(\[|\)\])"
            normalized_data = re.sub(regex, "", normalized_data)
        normalized_data = normalized_data.replace(" ", "")

        self.log(f"Normalized data:\n{normalized_data}")

        # get edges and labels using regex
        regex = r"([A-Za-z0-9]+)\s*-->\s*(?:\|([^|]+)\|\s*)?([A-Za-z0-9]+)"

        matches = re.findall(regex, normalized_data)
        for match in matches:
            parent_id = match[0]
            child_id = match[2]
            label = match[1] if match[1] else None
            parent_node = graph.get_node(parent_id)
            child_node = graph.get_node(child_id)
            if label:
                edge = parent_node >> label >> child_node
            else:
                edge = parent_node >> child_node
            self.log(f"Adding edge: {edge}")
        return graph

    def __extract_node_shape(self, node_label):
        """Extract node shape from node label."""
        node_shape = "rectangle"
        if node_label.startswith("["):
            node_shape = "rectangle"
            node_label = node_label[1:-1]
        elif node_label.startswith("("):
            node_shape = "circle"
            node_label = node_label[1:-1]
        elif node_label.startswith("{"):
            node_shape = "diamond"
            node_label = node_label[1:-1]
        return node_shape, node_label

import typing

from drawio.entities.base_entity import BaseEntity
from drawio.entities.drawio_config.drawio_config import DrawIOConfig

if typing.TYPE_CHECKING:
    from drawio.entities.graph.node import Node

DRAWIO_SHAPES = {
    "table": "mxgraph.dfd.data",
    "circle": "ellipse",
}


class Graph(BaseEntity):
    def __init__(self, single_node=None, graph_type="flowchart", name=None):
        super().__init__()
        self.name = name or "Graph Name"
        self.graph_type = graph_type
        if single_node is not None:
            single_node.graph = self
            self.nodes = [single_node]
        else:
            self.nodes: typing.List["Node"] = []
        self.edges = []

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def to_draw_io(self) -> str:
        """
        Returns a string that can be used to draw the graph in draw.io

        Example:
            ;Example:
            a->b
            b->edge label->c
            c->a

        """
        graph_string = ""
        for edge in self.edges:
            if edge.label:
                graph_string += f"{edge.parent.name}->{edge.label}->{edge.child.name}\n"
            else:
                graph_string += f"{edge.parent.name}->{edge.child.name}\n"
        return graph_string

    def to_draw_io_csv(self, drawio_config: DrawIOConfig = DrawIOConfig()) -> str:
        """
        Returns a CSV string that can be used to draw the graph in draw.io

        Example:
            ## Topology
            # label: %host%
            # namespace: csvimport-
            # connect: {
                        "from":"connected",
                        "to":"entry",
                        "style": "rounded=0;endArrow=none;endFill=0;startArrow=none;startFill=0;jumpStyle=sharp;"
                        }

            ## Shapes and their styles
            # stylename: type
            # styles: {
                        "server": "fontColor=#232F3E;fillColor=#232F3E;
                                    verticalLabelPosition=bottom;verticalAlign=top;align=center;
                                    html=1;
                                    shape=mxgraph.aws4.traditional_server;
                                    perimeter=none;
                                    strokeColor=#232F3E;
                                    aspect=fixed;
                                    whiteSpace=wrap;",
                        "node": "fontColor=#232F3E;gradientColor=#505863;
                                fillColor=#1E262E;
                                strokeColor=#ffffff;
                                dashed=0;
                                verticalLabelPosition=bottom;
                                verticalAlign=top;
                                align=center;
                                html=1;
                                fontSize=12;
                                fontStyle=0;
                                aspect=fixed;
                                shape=mxgraph.aws4.resourceIcon;
                                resIcon=mxgraph.aws4.general;",
                        "firewall": "fontColor=#232F3E;fillColor=#232F3E;
                                    verticalLabelPosition=bottom;
                                    verticalAlign=top;
                                    align=center;html=1;shape=mxgraph.aws4.generic_firewall;perimeter=none;strokeColor=#232F3E;aspect=fixed;whiteSpace=wrap;",\
            # "database": "fontColor=#232F3E;fillColor=#232F3E;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;shape=mxgraph.aws4.generic_database;perimeter=none;strokeColor=#232F3E;labelPosition=center;horizontal=1;aspect=fixed;whiteSpace=wrap;"}
            # ignore: entry,zone,type,connected
            # nodespacing: 40
            # levelspacing: 30
            # edgespacing: 30
            # layout: verticalflow
            ## CSV data starts below this line
            entry,zone,type,host,connected
            1,Internet,server,J2EE application server,3
            2,Extranet frontend,node,Node (extranet),4
            3,DMZ,firewall,Firewall 1,"5,6"
            4,DMZ,firewall,Firewall 2,"7,8,12"
            5,Warehouse,node,Node (Warehouse),9
            6,ITS department,node,Node (ITS),"10,11,12"
            7,PR department,node,Node (PR),12
            8,HR department,node,Node (HR),11
            9,Warehouse,server,Order system,
            10,Data storage,server,Data services,
            11,Data storage,database,Corporate database,
            12,Extranet backend,server,Extranet server,
        """

        graph_string = (
            "## type:csv\n## Build with Drawio-python\n# style: shape=%shape%\n"
        )
        graph_string += drawio_config.to_config_string()

        for node in self.nodes:
            child_edges = [edge for edge in self.edges if edge.parent == node]
            parent_edges = [edge for edge in self.edges if edge.child == node]
            input_nodes = [parent.parent for parent in parent_edges]
            output_nodes = [child.child for child in child_edges]
            input_ids = ",".join([str(node.id) for node in input_nodes])
            output_ids = ",".join([str(node.id) for node in output_nodes])
            shape = DRAWIO_SHAPES.get(node.shape, node.shape)

            if not child_edges:
                graph_string += (
                    f"{node.id},{node.name},,,,{node.color},{node.bg_color}\n"
                )
            else:
                # "node_id", "label", "edge_label", "shape", 'input_node', 'output_node'
                # TODO: handle edge labels here
                graph_string += f'{node.id},{node.name},,{shape},"{input_ids}","{output_ids}",{node.color},{node.bg_color}\n'

        return graph_string

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)

    def add_node(self, node):
        node.graph = self
        if node not in self.nodes:
            self.nodes.append(node)

    def get_node(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        else:
            self.log(
                f"Node with id {node_id} not found in graph"
                f"Valid node ids are: {', '.join([node.id for node in self.nodes])}"
            )
        return None

    def render(self, file_name: str, show: bool = False) -> str:
        from drawio.entities.renderers import renderers

        file_type = file_name.split(".")[-1]
        renderer = renderers.get(file_type)()
        if renderer is None:
            raise NotImplementedError(f"File type '{file_type}' is not supported.")
        return renderer.render(graph=self, output_file=file_name, show=show)

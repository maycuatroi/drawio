from drawio.entities.drawio_config.abstract_config import AbstractConfig
from drawio.entities.drawio_config.connect_config import ConnectConfig


class DrawIOConfig(AbstractConfig):
    def __init__(self, **kwargs):
        self.name_space = "drawio-python"
        self.label = "%node_name%"
        self.width = "auto"
        self.height = "auto"
        self.padding = 15
        self.nodespacing = 40
        self.levelspacing = 100
        self.edgespacing = 40
        self.layout = "auto"
        self.connect = []
        self.column_names = [
            "node_id",
            "node_name",
            "edge_label",
            "shape",
            "input_node",
            "output_node",
            "color",
            "bg_color",
        ]
        self.stylename = "shape"
        self.styles = {}
        self.add_connect(connect=ConnectConfig(from_id="node_id", to_id="output_node"))
        super().__init__(**kwargs)

    @property
    def ignore(self):
        """
        In the template, don't actually know what to do with this property
        """
        return self.column_names

    def add_connect(self, connect: ConnectConfig):
        self.connect.append(connect)

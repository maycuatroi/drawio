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
        self.column_names = []
        super().__init__(**kwargs)

    @property
    def ignore(self):
        """
        In the template, don't actually know what to do with this property
        """
        return self.column_names

    def add_connect(self, connect: ConnectConfig):
        self.connect.append(connect)

import json

from drawio.entities.drawio_config.abstract_config import AbstractConfig


class ConnectConfig(AbstractConfig):
    def __init__(self, from_id: str, to_id: str, **kwargs):
        self.from_id = from_id
        self.to_id = to_id
        self.style = "edgeStyle=orthogonalEdgeStyle;curved=1;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
        super().__init__(**kwargs)

    def to_config_string(self):
        """
        Example:
        connect: {"from": "manager", "to": "name", "invert": true, "label": "manages", "style": "curved=1;endArrow=blockThin;endFill=1;fontSize=11;"}
        """
        data = json.dumps(self.__dict__)
        # rename 'from_id' to 'from'
        data = data.replace('"from_id"', '"to"')
        # rename 'to_id' to 'to'
        data = data.replace('"to_id"', '"from"')
        return data

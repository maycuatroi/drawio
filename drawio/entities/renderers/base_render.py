import abc

from drawio.entities.base_entity import BaseEntity
from drawio.entities.graph.graph import Graph


class BaseRender(BaseEntity):
    file_type = None

    def __init__(self):
        super().__init__()
        self.show = False

    @abc.abstractmethod
    def _render(self, graph: "Graph", output_file: str):
        raise NotImplementedError

    def render(
        self, graph: "Graph", output_file: str = None, show: bool = False
    ) -> str:
        output_file = output_file or f"{graph.name}.{self.file_type}"
        self.log(f"Rendering {self.file_type} file")
        self.show = show
        output_file_name = self._render(graph, output_file=output_file)
        self.log(f"Rendered {self.file_type} file")
        return output_file_name

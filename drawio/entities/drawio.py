import abc

from diagrams.entities.graph import Graph


class DrawIO:
    def __init__(self):
        if not self._is_opened():
            self._open()

    @abc.abstractmethod
    def _is_opened(self):
        return False

    @abc.abstractmethod
    def _open(self):
        pass

    def show(self, g: Graph):
        pass

    @abc.abstractmethod
    def render_csv(self, csv_string):
        pass

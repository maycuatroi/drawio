import typing

from drawio.entities.erd.table import Table


class ERD:
    def __init__(self, tables: typing.List[Table]):
        self.tables = tables

    def to_drawio_text(self):
        """
        Example:
            Address
            -street: String
            -city: String
            -state: String
        """
        result = ""
        for table in self.tables:
            result += table.to_drawio_text()
            result += "\n"
        return result

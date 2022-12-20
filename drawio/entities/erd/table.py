#  Author: Nguyen Anh Binh - Binhna1
#  Created date:  2022 - 12 - 12

from diagrams.entities.erd.column import Column
from diagrams.entities.graph.node import Node


class Table(Node):
    def __init__(self, table_name: str, columns):
        super().__init__(table_name, shape="table")
        for i in range(len(columns)):
            col = columns[i]
            if isinstance(col, list) or isinstance(col, tuple):
                columns[i] = Column(col[0], col[1])
        self.columns = columns

    def to_drawio_text(self):
        """
        Example:
            Address
            -street: String
            -city: String
            -state: String
        """
        result = self.name + "\n"
        for column in self.columns:
            result += f"{column.column_name}: {column.column_type}\n"
        return result

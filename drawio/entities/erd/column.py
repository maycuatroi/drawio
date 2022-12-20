#  Author: Nguyen Anh Binh - Binhna1
#  Created date:  2022 - 12 - 12


class Column:
    def __init__(self, column_name: str, column_type: str):
        self.column_name = column_name
        self.column_type = column_type

    def __str__(self):
        return f"{self.column_name} ({self.column_type})"

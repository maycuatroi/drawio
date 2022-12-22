#  Author: Nguyen Anh Binh - Binhna1
#  Created date:  2022 - 12 - 12


class Column:
    def __init__(self, column_name: str, column_type: str, null_able: bool = False):
        self.column_name = column_name
        self.column_type = column_type
        self.null_able = null_able

    def __str__(self):
        return f"{self.column_name} ({self.column_type})"

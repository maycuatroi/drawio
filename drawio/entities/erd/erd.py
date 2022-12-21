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

    def export_table_schema(self, output_path):
        """
        Export tables schema to Excel file,
        1 table in 1 sheet
        Data contains:
            Table name
            Column name
            Column type

        """
        import pandas as pd

        writer = pd.ExcelWriter(output_path, engine="xlsxwriter")
        for i, table in enumerate(self.tables):
            columns = table.columns
            column_names = ["Column Name"] + [column.column_name for column in columns]
            column_types = ["Column Type"] + [column.column_type for column in columns]
            df = pd.DataFrame(
                {
                    "Column Name": column_names,
                    "Column Type": column_types,
                }
            )

            # insert table name to first row
            df.loc[-1] = [table.name, ""]  # adding a row
            df.index = df.index + 1  # shifting index
            df = df.sort_index()  # sorting by index
            # header color is green
            table_short_name = f"{i+1}. {table.name[:20]}"
            df.to_excel(writer, sheet_name=table_short_name, index=False, header=False)
            worksheet = writer.sheets[table_short_name]
            worksheet.set_column("A:A", 30)
            worksheet.set_column("B:B", 30)
            worksheet.merge_range("A1:B1", table.name)

            # header color is green
            format1 = writer.book.add_format({"bg_color": "#C6EFCE"})
            worksheet.conditional_format(
                "A1:B1", {"type": "no_blanks", "format": format1}
            )
            # color is blue
            format2 = writer.book.add_format({"bg_color": "#BDD7EE"})
            worksheet.conditional_format(
                "A2:B2", {"type": "no_blanks", "format": format2}
            )

        writer.save()

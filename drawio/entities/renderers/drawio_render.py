from drawio.entities.drawio_browser import DrawIOBrowser
from drawio.entities.graph.graph import Graph
from drawio.entities.renderers.base_render import BaseRender


class DrawIORender(BaseRender):
    file_type = "drawio"

    def _render(self, graph: "Graph", output_file: str, show: bool = False):
        csv_string = graph.to_draw_io_csv()
        print(csv_string)
        drawio_browser = DrawIOBrowser(hide=not show)
        drawio_browser.render(draw_io_string=csv_string, graph_name=graph.name)
        # export to file
        drawio_browser.export(output_file)

        if show:
            input("Press Enter to continue...")

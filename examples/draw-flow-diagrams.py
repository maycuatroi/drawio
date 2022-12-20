"""
Mermaid
graph TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
"""

from drawio import Graph, Node
from drawio.entities.drawio_browser import DrawIOBrowser

node_a = Node("Christmas", shape="rectangle")
node_b = Node("Go shopping", shape="rectangle")
node_c = Node("Let me think", shape="oval")
node_d = Node("Laptop", shape="rectangle")
node_e = Node("iPhone", shape="rectangle")
node_f = Node("Car", shape="rectangle")

graph = Graph()
graph.add_nodes([node_a, node_b, node_c, node_d, node_e, node_f])
node_a >> "Get money" >> node_b
node_b >> node_c >> "One" >> node_d
node_c >> "Two" >> node_e
node_c >> "Three" >> node_f

csv_string = graph.to_draw_io_csv()
print(csv_string)
drawio_browser = DrawIOBrowser()
drawio_browser.render(csv_string)
input("Press enter to exit")

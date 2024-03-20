from drawio.entities.renderers.drawio_render import DrawIORender
from drawio.entities.renderers.pdf_render import PDFRender

__renders = [PDFRender, DrawIORender]
renderers = dict((render.file_type, render) for render in __renders)

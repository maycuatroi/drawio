from drawio.entities.renderers.pdf_render import PDFRender

__renders = [PDFRender]
renderers = dict((render.file_type, render) for render in __renders)

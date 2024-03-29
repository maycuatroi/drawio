import logging


class DrawioLogger(logging.Logger):
    def __init__(self, name="Drawio", level=logging.DEBUG):
        super().__init__(name, level)
        self.setLevel(level)
        self.addHandler(logging.StreamHandler())

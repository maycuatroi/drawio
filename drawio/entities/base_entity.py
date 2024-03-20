from drawio.entities.logger import DrawioLogger


class BaseEntity:
    def __init__(self):
        self.logger = DrawioLogger("drawio")

    def log(self, message):
        self.logger.debug(message)

from glob import glob

from drawio.entities.drawio import DrawIO
import pywinauto


class DrawIOApp(DrawIO):
    def __init__(self):
        self.window = self.find_drawio_app_window()
        self.hw = self.window.handle
        super().__init__()

    def find_drawio_app_window(self):
        windows = pywinauto.findwindows.find_windows(title_re=".*drawio.*")
        if not windows:
            return None
        return pywinauto.Desktop(backend="uia").window(handle=windows[0])

    def _is_opened(self):
        return self.window

    def __find_drawio_execute_path(self):
        window_app_paths = glob(
            r"C:\Program Files\WindowsApps\draw.io*", recursive=True
        )
        if not window_app_paths:
            raise Exception("Draw.io is not installed")
        return window_app_paths[0]

    def _open(self):
        path = self.__find_drawio_execute_path()
        pywinauto.application.Application().start(path)

    def render_csv(self, csv_string):
        # window to top
        # self.window.set_focus()
        # print control
        self.window.print_control_identifiers()

        # find "Insert (Doubleclick to insert text)"
        insert_button = self.window.child_window(
            title="Insert (Doubleclick to insert text)"
        )
        # click
        insert_button.click_input()

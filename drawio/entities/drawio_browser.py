from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from drawio.entities.drawio import DrawIO


class DrawIOBrowser(DrawIO):
    def _is_opened(self):
        return False

    def __find_decide_later(self):
        spans = self.driver.find_elements(By.TAG_NAME, "span")
        for span in spans:
            if span.text == "Decide later":
                return span
        raise NoSuchElementException("Decide later not found")

    def _open(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://app.drawio.net/")
        # wait to load span Decide later
        decide_later_node = WebDriverWait(self.driver, 5).until(
            lambda driver: self.__find_decide_later()
        )
        decide_later_node.click()

    def __click_insert_advance(self):
        sleep(1)
        self.driver.find_element(
            By.CLASS_NAME, "geSprite-plus"
        ).click()  # Insert (Doubleclick to insert text)
        self.__click_pop_up_items("Advanced")

    def __click_pop_up_items(self, name):
        def _action():
            pop_ups = self.driver.find_elements(By.CLASS_NAME, "mxPopupMenuItem")
            for pop_up in pop_ups:
                if pop_up.text == name:
                    pop_up.click()
                    return True
            raise NoSuchElementException(f"{name} not found")

        WebDriverWait(self.driver, 5).until(lambda _: _action())

    def __click_button(self, name):
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.text == name:
                button.click()
                return True
        raise NoSuchElementException(f"{name} not found")

    def render_csv(self, csv_string):
        # click on "Insert (Doubleclick to insert text)"
        # find element by title
        self.__click_insert_advance()
        self.__click_pop_up_items("CSV...")
        text_area = self.driver.find_element(By.TAG_NAME, "textarea")  # CSV text area
        # clear text area
        text_area.clear()
        text_area.set_attribute("value", csv_string)
        self.__click_button("Import")

    def __init__(self):
        self.driver = None

        super().__init__()

    def render_text(self, text, type: str = "list"):
        self.__click_insert_advance()
        self.driver.find_element(
            By.XPATH, "/html/body/div[11]/table/tbody/tr[1]/td[2]"
        ).click()  # Insert Text
        text_area = self.driver.find_element(
            By.XPATH, "/html/body/div[11]/div/textarea"
        )  # Text text area
        # clear text area
        text_area.clear()
        text_area.send_keys(text)
        if type != "list":
            raise NotImplementedError("Only list type is supported")
        self.driver.find_element(
            By.XPATH, "/html/body/div[11]/div/button[2]"
        ).click()  # Import

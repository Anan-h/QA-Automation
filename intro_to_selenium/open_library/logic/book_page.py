from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class BookPage(BaseAppPage):
    FIVE_STAR_RATING_BTN = "//div[@id='test-body-mobile']//div[3]//label[@class='star star-5 ']"
    CLEAR_RATING_MSG = "//button[@class='star-messaging']"
    NOTES_BUTTON = "//div[5]/div[2]//div[text()='Notes']"
    NOTES_TEXT_AREA = "//div[@id='colorbox']//textarea"
    SAVE_NOTES_BUTTON = "//div[@id='colorbox']//button[@class='update-note-button cta-btn cta-btn--shell']"
    BOOK_TITLE = "//div[@class='work-title-and-author desktop']//h1[@class='work-title']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._top_rate = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.FIVE_STAR_RATING_BTN)))
            self._notes_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.NOTES_BUTTON)))
            self._book_title=WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.BOOK_TITLE)))
        except NoSuchElementException as e:
            print(e)

    def rate_as_top_rating(self):
        self._top_rate.click()

    def get_rating_confirmation_message(self):
        try:
            msg = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.CLEAR_RATING_MSG)))
            return msg.text
        except NoSuchElementException as e:
            print(e)

    def fill_notes_text_area(self, note):
        try:
            text_area = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.NOTES_TEXT_AREA)))
            text_area.send_keys(note)
        except NoSuchElementException as e:
            print(e)

    def click_on_save_note_button(self):
        try:
            save_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SAVE_NOTES_BUTTON)))
            save_button.click()
        except NoSuchElementException as e:
            print(e)

    def adding_note_flow(self, note):
        self.fill_notes_text_area(note)
        self.click_on_save_note_button()

    def book_title_is_visible(self):
        return self._book_title.is_displayed()

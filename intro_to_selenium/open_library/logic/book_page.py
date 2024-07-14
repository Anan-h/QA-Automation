import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from intro_to_selenium.open_library.logic.base_app_page import BaseAppPage


class BookPage(BaseAppPage):
    FIVE_STAR_RATING_BTN = "//div[@class='panel']//div[@class='lists-widget-container']//label[@property='bestRating']"
    CLEAR_RATING_BUTTON = "//button[@class='star-messaging']"
    NOTES_BUTTON = "//div[@class='panel']/div/div[@class='modal-links']//a[@class='notes-modal-link icon-link']"
    NOTES_TEXT_AREA = "//div[@id='colorbox']//textarea"
    SAVE_NOTES_BUTTON = "//div[@id='colorbox']//button[@class='update-note-button cta-btn cta-btn--shell']"
    BOOK_TITLE = "//div[@class='work-title-and-author desktop']//h1[@class='work-title']"
    NOTE_SAVED_CONFIRMATION = "//div[@class='toast-container']"

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._book_title = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.BOOK_TITLE)))
        except TimeoutException as e:
            logging.error(e)

    def rate_as_top_rating(self):
        """
        A function that rates a book as best rating (five stars )
        :return:
        """
        try:
            top_rate = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.FIVE_STAR_RATING_BTN)))
            top_rate.click()
            logging.info("rated as best rating ")
        except TimeoutException as e:
            logging.error(e)

    def clear_rating_button_is_visible(self):
        """
        A function that checks if the button clear rating is visible
        :return: True or False
        """
        try:
            clear_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CLEAR_RATING_BUTTON)))
            if clear_button.is_displayed():
                logging.info("the clear rating button was displayed")
            else:
                logging.warning("the clear rating button was not displayed")
            return clear_button.is_displayed()
        except TimeoutException as e:
            logging.error(e)

    def click_on_clear_rating_button(self):
        """
        A function that clicks on the clear rating button
        :return:
        """
        try:
            clear_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.CLEAR_RATING_BUTTON)))
            clear_button.click()
            logging.info("clicked on the clear rating button")
        except TimeoutException as e:
            logging.error(e)

    def fill_notes_text_area(self, note):
        """
        A function that clears the notes text area and insert a new note that is given earlier
        :param note: the content of the note
        :return:
        """
        try:
            text_area = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.NOTES_TEXT_AREA)))
            text_area.clear()
            logging.info("cleared notes text area")
            text_area.send_keys(note)
            logging.info(f"{note} inserted into notes text area")

        except TimeoutException as e:
            logging.error(e)

    def click_on_save_note_button(self):
        """
        A function that clicks on the save button , after inserting a certain note in the text area
        :return:
        """
        try:
            save_button = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.SAVE_NOTES_BUTTON)))
            save_button.click()
            logging.info("clicked on save button")
        except TimeoutException as e:
            logging.error(e)

    def adding_note_flow(self, note):
        """
        A function that performs the whole process of inserting a note and saving it
        :param note: the content of the note
        :return:
        """
        self.click_on_notes_button()
        self.fill_notes_text_area(note)
        self.click_on_save_note_button()

    def book_title_is_visible(self):
        """
        A function that checks if the book title is displayed in the screen
        :return: True or False
        """
        if self._book_title.is_displayed():
            logging.info("the book title was displayed")
        else:
            logging.warning("the book title was not displayed ")
        return self._book_title.is_displayed()

    def click_on_notes_button(self):
        """
        A function that clicks on the notes button in order to add a note
        :return:
        """
        try:
            notes_button = WebDriverWait(self._driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.NOTES_BUTTON)))
            notes_button.click()
            logging.info("clicked on notes button")
        except TimeoutException as e:
            logging.error(e)

    def confirmation_message_appearance(self):
        """
        A function that checks if the message that confirms that the note is added , is displayed
        :return: True or false
        """
        try:
            msg = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.NOTE_SAVED_CONFIRMATION))
            )
            if msg.is_displayed():
                logging.info("the adding note confirmation message was displayed")
            else:
                logging.warning("the adding note confirmation message was not displayed")
            return msg.is_displayed()
        except TimeoutException as e:
            print(e)

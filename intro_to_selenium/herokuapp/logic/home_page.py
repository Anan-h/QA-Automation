from selenium.webdriver.common.by import By
from intro_to_selenium.herokuapp.logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    ADD_REMOVE_ELEMENTS = '//a[text() = "Add/Remove Elements"]'
    BROKEN_IMAGES = '//a[text() = "Broken Images"]'
    CHALLENGING_DOM = '//a[text() = "Challenging DOM"]'
    CHECKBOXES = '//a[text() = "Checkboxes"]'
    CONTEXT_MENU = '//a[text() = "Context Menu"]'
    DIGEST_AUTHENTICATION = '//a[text() = "Digest Authentication"]'
    DISAPPEARING_ELEMENTS = '//a[text() = "Disappearing Elements"]'
    DRAG_AND_DROP = '//a[text() = "Drag and Drop"]'
    DROPDOWN = '//a[text() = "Dropdown"]'
    DYNAMIC_CONTENT = '//a[text() = "Dynamic Content"]'
    DYNAMIC_CONTROLS = '//a[text() = "Dynamic Controls"]'
    DYNAMIC_LOADING = '//a[text() = "Dynamic Loading"]'
    ENTRY_AD = '//a[text() = "Entry Ad"]'
    EXIT_INTENT = '//a[text() = "Exit Intent"]'
    FILE_DOWNLOAD = '//a[text() = "File Download"]'
    FILE_UPLOAD = '//a[text() = "File Upload"]'
    FLOATING_MENU = '//a[text() = "Floating Menu"]'
    FORGOT_PASSWORD = '//a[text() = "Forgot Password"]'
    FORM_AUTHENTICATION = '//a[text() = "Form Authentication"]'
    FRAMES = '//a[text() = "Frames"]'
    GEOLOCATION = '//a[text() = "Geolocation"]'
    HORIZONTAL_SLIDER = '//a[text() = "Horizontal Slider"]'
    HOVERS = '//a[text() = "Hovers"]'
    INFINITE_SCROLL = '//a[text() = "Infinite Scroll"]'
    INPUTS = '//a[text() = "Inputs"]'
    JQUERY_UI_MENUS = '//a[text() = "JQuery UI Menus"]'
    JAVASCRIPT_ALERTS = '//a[text() = "JavaScript Alerts"]'
    JAVASCRIPT_ONLOAD_EVENT_ERROR = '//a[text() = "JavaScript onload event error"]'
    KEY_PRESSES = '//a[text() = "Key Presses"]'
    LARGE_AND_DEEP_DOM = '//a[text() = "Large & Deep DOM"]'
    MULTIPLE_WINDOWS = '//a[text() = "Multiple Windows"]'
    NESTED_FRAMES = '//a[text() = "Nested Frames"]'
    NOTIFICATION_MESSAGES = '//a[text() = "Notification Messages"]'
    REDIRECT_LINK = '//a[text() = "Redirect Link"]'
    SECURE_FILE_DOWNLOAD = '//a[text() = "Secure File Download"]'
    SHADOW_DOM = '//a[text() = "Shadow DOM"]'
    SHIFTING_CONTENT = '//a[text() = "Shifting Content"]'
    SLOW_RESOURCES = '//a[text() = "Slow Resources"]'
    SORTABLE_DATA_TABLES = '//a[text() = "Sortable Data Tables"]'
    STATUS_CODES = '//a[text() = "Status Codes"]'
    TYPOS = '//a[text() = "Typos"]'
    WYSIWYG_EDITOR = '//a[text() = "WYSIWYG Editor"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_remove_elements = self._driver.find_element(By.XPATH, self.ADD_REMOVE_ELEMENTS)
        self._broken_images = self._driver.find_element(By.XPATH, self.BROKEN_IMAGES)
        self._challenging_dom = self._driver.find_element(By.XPATH, self.CHALLENGING_DOM)
        self._checkboxes = self._driver.find_element(By.XPATH, self.CHECKBOXES)
        self._context_menu = self._driver.find_element(By.XPATH, self.CONTEXT_MENU)
        self._digest_authentication = self._driver.find_element(By.XPATH, self.DIGEST_AUTHENTICATION)
        self._disappearing_elements = self._driver.find_element(By.XPATH, self.DISAPPEARING_ELEMENTS)
        self._drag_and_drop = self._driver.find_element(By.XPATH, self.DRAG_AND_DROP)
        self._dropdown = self._driver.find_element(By.XPATH, self.DROPDOWN)
        self._dynamic_content = self._driver.find_element(By.XPATH, self.DYNAMIC_CONTENT)
        self._dynamic_controls = self._driver.find_element(By.XPATH, self.DYNAMIC_CONTROLS)
        self._dynamic_loading = self._driver.find_element(By.XPATH, self.DYNAMIC_LOADING)
        self._entry_ad = self._driver.find_element(By.XPATH, self.ENTRY_AD)
        self._exit_intent = self._driver.find_element(By.XPATH, self.EXIT_INTENT)
        self._file_download = self._driver.find_element(By.XPATH, self.FILE_DOWNLOAD)
        self._file_upload = self._driver.find_element(By.XPATH, self.FILE_UPLOAD)
        self._floating_menu = self._driver.find_element(By.XPATH, self.FLOATING_MENU)
        self._forgot_password = self._driver.find_element(By.XPATH, self.FORGOT_PASSWORD)
        self._form_authentication = self._driver.find_element(By.XPATH, self.FORM_AUTHENTICATION)
        self._frames = self._driver.find_element(By.XPATH, self.FRAMES)
        self._geolocation = self._driver.find_element(By.XPATH, self.GEOLOCATION)
        self._horizontal_slider = self._driver.find_element(By.XPATH, self.HORIZONTAL_SLIDER)
        self._hovers = self._driver.find_element(By.XPATH, self.HOVERS)
        self._infinite_scroll = self._driver.find_element(By.XPATH, self.INFINITE_SCROLL)
        self._inputs = self._driver.find_element(By.XPATH, self.INPUTS)
        self._jquery_ui_menus = self._driver.find_element(By.XPATH, self.JQUERY_UI_MENUS)
        self._javascript_alerts = self._driver.find_element(By.XPATH, self.JAVASCRIPT_ALERTS)
        self._javascript_onload_event_error = self._driver.find_element(By.XPATH, self.JAVASCRIPT_ONLOAD_EVENT_ERROR)
        self._key_presses = self._driver.find_element(By.XPATH, self.KEY_PRESSES)
        self._large_and_deep_dom = self._driver.find_element(By.XPATH, self.LARGE_AND_DEEP_DOM)
        self._multiple_windows = self._driver.find_element(By.XPATH, self.MULTIPLE_WINDOWS)
        self._nested_frames = self._driver.find_element(By.XPATH, self.NESTED_FRAMES)
        self._notification_messages = self._driver.find_element(By.XPATH, self.NOTIFICATION_MESSAGES)
        self._redirect_link = self._driver.find_element(By.XPATH, self.REDIRECT_LINK)
        self._secure_file_download = self._driver.find_element(By.XPATH, self.SECURE_FILE_DOWNLOAD)
        self._shadow_dom = self._driver.find_element(By.XPATH, self.SHADOW_DOM)
        self._shifting_content = self._driver.find_element(By.XPATH, self.SHIFTING_CONTENT)
        self._slow_resources = self._driver.find_element(By.XPATH, self.SLOW_RESOURCES)
        self._sortable_data_tables = self._driver.find_element(By.XPATH, self.SORTABLE_DATA_TABLES)
        self._status_codes = self._driver.find_element(By.XPATH, self.STATUS_CODES)
        self._typos = self._driver.find_element(By.XPATH, self.TYPOS)
        self._wysiwyg_editor = self._driver.find_element(By.XPATH, self.WYSIWYG_EDITOR)

    def click_on_add_remove_link(self):
        self._add_remove_elements.click()

    def click_on_broken_images_link(self):
        self._broken_images.click()

    def click_on_challenging_dom_link(self):
        self._challenging_dom.click()

    def click_on_checkboxes_link(self):
        self._checkboxes.click()

    def click_on_context_menu_link(self):
        self._context_menu.click()

    def click_on_digest_authentication_link(self):
        self._digest_authentication.click()

    def click_on_disappearing_elements_link(self):
        self._disappearing_elements.click()

    def click_on_drag_and_drop_link(self):
        self._drag_and_drop.click()

    def click_on_dropdown_link(self):
        self._dropdown.click()

    def click_on_dynamic_content_link(self):
        self._dynamic_content.click()

    def click_on_dynamic_controls_link(self):
        self._dynamic_controls.click()

    def click_on_dynamic_loading_link(self):
        self._dynamic_loading.click()

    def click_on_entry_ad_link(self):
        self._entry_ad.click()

    def click_on_exit_intent_link(self):
        self._exit_intent.click()

    def click_on_file_download_link(self):
        self._file_download.click()

    def click_on_file_upload_link(self):
        self._file_upload.click()

    def click_on_floating_menu_link(self):
        self._floating_menu.click()

    def click_on_forgot_password_link(self):
        self._forgot_password.click()

    def click_on_form_authentication_link(self):
        self._form_authentication.click()

    def click_on_frames_link(self):
        self._frames.click()

    def click_on_geolocation_link(self):
        self._geolocation.click()

    def click_on_horizontal_slider_link(self):
        self._horizontal_slider.click()

    def click_on_hovers_link(self):
        self._hovers.click()

    def click_on_infinite_scroll_link(self):
        self._infinite_scroll.click()

    def click_on_inputs_link(self):
        self._inputs.click()

    def click_on_jquery_ui_menus_link(self):
        self._jquery_ui_menus.click()

    def click_on_javascript_alerts_link(self):
        self._javascript_alerts.click()

    def click_on_javascript_onload_event_error_link(self):
        self._javascript_onload_event_error.click()

    def click_on_key_presses_link(self):
        self._key_presses.click()

    def click_on_large_and_deep_dom_link(self):
        self._large_and_deep_dom.click()

    def click_on_multiple_windows_link(self):
        self._multiple_windows.click()

    def click_on_nested_frames_link(self):
        self._nested_frames.click()

    def click_on_notification_messages_link(self):
        self._notification_messages.click()

    def click_on_redirect_link(self):
        self._redirect_link.click()

    def click_on_secure_file_download_link(self):
        self._secure_file_download.click()

    def click_on_shadow_dom_link(self):
        self._shadow_dom.click()

    def click_on_shifting_content_link(self):
        self._shifting_content.click()

    def click_on_slow_resources_link(self):
        self._slow_resources.click()

    def click_on_sortable_data_tables_link(self):
        self._sortable_data_tables.click()

    def click_on_status_codes_link(self):
        self._status_codes.click()

    def click_on_typos_link(self):
        self._typos.click()

    def click_on_wysiwyg_editor_link(self):
        self._wysiwyg_editor.click()

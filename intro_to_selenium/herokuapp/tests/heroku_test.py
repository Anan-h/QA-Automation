import unittest
from intro_to_selenium.herokuapp.infra.browser_wrapper import BrowserWrapper
from intro_to_selenium.herokuapp.infra.config_provider import ConfigProvider
from intro_to_selenium.herokuapp.logic.add_remove_elements import AddRemoveElements
from intro_to_selenium.herokuapp.logic.challenging_dom import ChallengingDom
from intro_to_selenium.herokuapp.logic.check_boxes import CheckBoxes
from intro_to_selenium.herokuapp.logic.context_menu import ContextMenu
from intro_to_selenium.herokuapp.logic.disappearing_elements import DisappearingElements
from intro_to_selenium.herokuapp.logic.drag_and_drop import DragAndDrop
from intro_to_selenium.herokuapp.logic.dropdown_page import DropDownPage
from intro_to_selenium.herokuapp.logic.home_page import HomePage


class HerokuTest(unittest.TestCase):
    config = ConfigProvider.load_from_file('../config.json')

    def setUp(self):
        self.driver = BrowserWrapper().get_driver(self.config["url"])
        self.driver.maximize_window()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_add_remove_page(self):
        self.home_page.click_on_add_remove_link()
        add_remove = AddRemoveElements(self.driver)
        # add_remove.click_on_add_btn()
        add_remove.click_on_delete_button(5)

    def test_challenging_dom(self):
        self.home_page.click_on_challenging_dom_link()
        challenge = ChallengingDom(self.driver)
        challenge.click_on_one_delete_btn()
        url = challenge.get_current_url()
        self.assertEqual(url, "https://the-internet.herokuapp.com/challenging_dom#delete")

    def test_check_box(self):
        self.home_page.click_on_checkboxes_link()
        check = CheckBoxes(self.driver)
        check.select_first()
        check.select_second()
        self.assertTrue(check._box1.is_selected())
        self.assertFalse(check._box2.is_selected())

    def test_context_menu(self):
        self.home_page.click_on_context_menu_link()
        menu = ContextMenu(self.driver)
        menu.right_click_on_hot_spot()

    def test_disappearing_elements(self):
        self.home_page.click_on_disappearing_elements_link()
        dis = DisappearingElements(self.driver)
        elem = dis.gallery_button_appearance()
        self.assertTrue(elem.is_displayed())

    def test_drag_and_drop(self):
        self.home_page.click_on_drag_and_drop_link()
        dd = DragAndDrop(self.driver)
        dd.drag_a_to_b()

    def test_dropdown(self):
        self.home_page.click_on_dropdown_link()
        dd = DropDownPage(self.driver)
        dd.select_from_dropdown()


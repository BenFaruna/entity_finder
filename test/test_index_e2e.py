import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class E2ETests(unittest.TestCase):

    def setUp(self):
        service = Service("chromedriver_win32/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:5000")

    def tearDown(self):
        self.driver.quit()

    def _find(self, val):
        return self.driver.find_element(By.CSS_SELECTOR, f'[data-test-id="{val}"')

    def test_browser_title_contains_app_name(self):
        self.assertIn("Named Entity", self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual("Named Entity Finder", heading)

    def test_page_has_input_for_text(self):
        input_element = self._find("input-text")
        self.assertIsNotNone(input_element)

    def test_page_has_button_for_submitting_text(self):
        submit_button = self._find("submit-button")
        self.assertIsNotNone(submit_button)

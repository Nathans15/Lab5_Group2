
# Imports
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SeleniumClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the browser driver
        cls.browser = webdriver.Chrome()
        # Maximize the browser window
        cls.browser.maximize_window()
        sleep(3)

    def test_to_find_item(self):

        # Open the following URL in the browser
        self.browser.get("https://magento.softwaretestingboard.com/")
        sleep(3)

        # Click on Women
        # Find the women tab via XPATH using the find element method
        women_tab = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/nav/ul/li[2]/a/span[2]')
        # click register tab
        women_tab.click()
        sleep(1)

        # Click on Tops

        # Click on Hoodies & Sweatshirts

        # Select the appropriate Style, Size, Price Range, Color and Material

    def test_to_add_item_to_cart(self):

        # Select any single dress (if there are multiple depending upon your selection) and click on Add to cart
        # [ You may have to switch to frame]

        # Click the “cart icon”

    def test_to_checkout(self):

        # Click on the “Proceed to Checkout” Button

        # Assert the “Order summary”. Your shopping cart should show the dress selected by you

        # Finally close the browser
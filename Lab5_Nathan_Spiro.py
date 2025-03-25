
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

    def testCase(self):

        # Click on Women -> Tops -> Hoodies & Sweatshirts

        # Select the appropriate Style, Size, Price Range, Color and Material

        # Select any single dress (if there are multiple depending upon your selection) and click on Add to cart
        # [ You may have to switch to frame]

        # Click the “cart icon”

        # Click on the “Proceed to Checkout” Button

        # Assert the “Order summary”. Your shopping cart should show the dress selected by you

        # Finally close the browser
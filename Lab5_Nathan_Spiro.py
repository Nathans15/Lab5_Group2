
# Imports
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains




class SeleniumClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # Initialize the browser driver
        cls.driver = webdriver.Chrome()
        # Maximize the browser window
        cls.driver.maximize_window()
        sleep(3)

    def test_to_find_item(self):

        # Create the object driver
        driver = self.driver

        # Open the following URL in the browser
        driver.get("https://magento.softwaretestingboard.com/")
        sleep(3)

        # Create an ActionChains Object
        action = ActionChains(driver)

        # Hover cursor over the Women tab
        # Find the women tab via XPATH using the find element method
        women_tab = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/nav/ul/li[2]/a/span[2]')
        # Hover cursor over the women tab using action chains
        action.move_to_element(women_tab).perform()
        sleep(1)

        # Hover cursor on Tops
        tops_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a/span[2]')
        # Hover cursor over the tops option using action chains
        action.move_to_element(tops_option).perform()
        sleep(1)

        # Click on Hoodies & Sweatshirts
        # Find the Hoodies & Sweatshirts option via XPATH using the find element method
        hoodies_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[2]/a/span')
        # Click on Hoodies & Sweatshirts
        hoodies_option.click()
        sleep(1)

        # Select the appropriate Style, Size, Price Range, Color and Material
        # Style (Pullover)
        style = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[1]')
        style.click()

        style_pullover = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/ol/li[3]/a')
        style_pullover.click()

        # Size (M)
        size = driver.find_element(By.XPATH, '')
        size.click()

        size_m = driver.find_element(By.XPATH, '')
        size_m.click()

        # Price Range (50 - 59)
        price = driver.find_element(By.XPATH, '')
        price.click()

        price_range = driver.find_element(By.XPATH, '')
        price_range.click()

        # Color (Purple)
        color = driver.find_element(By.XPATH, '')
        color.click()

        color_purple = driver.find_element(By.XPATH, '')
        color_purple.click()

        # Material (Polyester)
        material = driver.find_element(By.XPATH, '')
        material.click()

        material_polyester = driver.find_element(By.XPATH, '')
        material_polyester.click()

    #def test_to_add_item_to_cart(self):

        # Select any single dress (if there are multiple depending upon your selection) and click on Add to cart
        # [ You may have to switch to frame]

        # Click the “cart icon”

    #def test_to_checkout(self):

        # Click on the “Proceed to Checkout” Button

        # Assert the “Order summary”. Your shopping cart should show the dress selected by you

        # Finally close the browser
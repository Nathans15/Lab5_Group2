
# Imports
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class SeleniumClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Initialize the browser driver
        cls.driver = webdriver.Chrome()
        # Maximize the browser window
        cls.driver.maximize_window()
        sleep(3)

    def test_A_to_find_item(self):
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
        sleep(2)

        # Hover cursor on Tops
        tops_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a/span[2]')
        # Hover cursor over the tops option using action chains
        action.move_to_element(tops_option).perform()
        sleep(2)

        # Click on Hoodies & Sweatshirts
        # Find the Hoodies & Sweatshirts option via XPATH using the find element method
        hoodies_option = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[2]/a/span')
        # Click on Hoodies & Sweatshirts
        hoodies_option.click()
        sleep(2)

        # Select the appropriate Style, Size, Price Range, Color and Material
        # Style (Pullover)
        style = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[1]')
        style.click()

        style_pullover = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[1]/div[2]/ol/li[3]/a')
        style_pullover.click()
        sleep(2)

        # Size (M)
        #size = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[2]/div[1]')
        size = driver.find_element(By.XPATH, "//div[normalize-space()='Size']")
        size.click()
        sleep(2)

        #size_m = driver.find_element(By.XPATH, "//a[@aria-label='M']//div[contains(@class,'swatch-option text')][normalize-space()='M']").click()
        size_m = driver.find_element(By.XPATH,"//a[@aria-label='M']//div[contains(@class,'swatch-option text')][normalize-space()='M']")
        size_m.click()
        sleep(2)

        # Price Range (50 - 59)
        price = driver.find_element(By.XPATH, "//div[normalize-space()='Price']")
        price.click()

        price_range = driver.find_element(By.XPATH, "//span[normalize-space()='$59.99']")
        price_range.click()
        sleep(2)

        # Color (Purple)
        color = driver.find_element(By.XPATH, "//div[normalize-space()='Color']")
        color.click()

        color_purple = driver.find_element(By.XPATH, "//a[@aria-label='Purple']//div[contains(@class,'swatch-option color')]")
        color_purple.click()
        sleep(2)

        # Material (Polyester)
        material = driver.find_element(By.XPATH, "//div[normalize-space()='Material']")
        material.click()
        sleep(2)

        material_polyester = driver.find_element(By.XPATH, "//a[contains(text(),'Polyester')]")
        material_polyester.click()
        sleep(2)

        # Selected item (Autumn Pullie)
        #autumn_pullie = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[10]/div/a')
        autumn_pullie = driver.find_element(By.XPATH, "//a[@class='product-item-link']")
        autumn_pullie.click()
        sleep(1)

    def test_B_add_to_cart_and_checkout(self):
        # Create the object driver
        driver = self.driver

        driver.get("https://magento.softwaretestingboard.com/autumn-pullie.html")
        sleep(3)

        # Might need to switch the frame (Maybe not)

        # Pick size (M)
        autumn_pullie_size = driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']")
        autumn_pullie_size.click()
        sleep(3)

        # Pick color (Purple)
        autumn_pullie_color = driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']")
        autumn_pullie_color.click()
        sleep(5)

        # Find and click add to cart button
        add_cart_button = driver.find_element(By.ID, "product-addtocart-button")
        add_cart_button.click()
        sleep(3)

        # Find and click the cart icon (Located top right of page)
        cart_button = driver.find_element(By.XPATH, "//a[@class='action showcart']")
        cart_button.click()
        sleep(3)

        # Find and click the “Proceed to Checkout” Button
        checkout_button = driver.find_element(By.XPATH, '//*[@id="top-cart-btn-checkout"]')
        checkout_button.click()
        sleep(3)

        # Assert the “Order summary” with assertEqual, Your shopping cart should show the item selected by you
        order_summary = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[1]')
        order_summary.click()
        sleep(3)

        view_details = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div/div[2]/aside/div[2]/div/div/div[1]/div/div[2]/div/ol/li/div/div/div[2]/span')
        view_details.click()
        sleep(3)

        product_item_name = driver.find_element(By.CSS_SELECTOR, ".product-item-name")
        product_details_colour = driver.find_element(By.CSS_SELECTOR, "dd.values:nth-child(4)")
        product_details_size = driver.find_element(By.CSS_SELECTOR, "dd.values:nth-child(2)")

        self.assertEqual(product_item_name.text, "Autumn Pullie")
        self.assertEqual(product_details_size.text, "M")
        self.assertEqual(product_details_colour.text, "Purple")


    # Finally close the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


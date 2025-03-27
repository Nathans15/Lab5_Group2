
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

    def test_to_find_item(self):

        # Create the object driver
        driver = self.driver

        # Open the following URL in the browser
        driver.get("https://magento.softwaretestingboard.com/")
        sleep(3)

        # switch to frame 0
        #driver.switch_to.frame(0)

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
        size = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[2]/div[1]')
        size.click()
        sleep(2)

        size_m = driver.find_element(By.XPATH, "//a[@aria-label='M']//div[contains(@class,'swatch-option text')][normalize-space()='M']")
        #action.click(size_m).perform()
        size_m.click()
        sleep(2)

        # Price Range (50 - 59)
        price = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[11]/div[1]')
        price.click()

        price_range = driver.find_element(By.XPATH, "//span[normalize-space()='$59.99']")
        #action.click(price_range).perform()
        price_range.click()
        sleep(2)

        # Color (Purple)
        color = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[4]/div[1]')
        color.click()

        color_purple = driver.find_element(By.XPATH, "//a[@aria-label='Purple']//div[contains(@class,'swatch-option color')]")
        #action.click(color_purple).perform()
        color_purple.click()
        sleep(2)

        # Material (Polyester)
        material = driver.find_element(By.XPATH, '//*[@id="narrow-by-list"]/div[7]/div[1]')
        material.click()
        sleep(2)

        material_polyester = driver.find_element(By.XPATH, "//a[contains(text(),'Polyester')]")
        #action.click(material_polyester).perform()
        material_polyester.click()
        sleep(2)

    def test_to_add_item_to_cart(self):

        # ---------------THIS PART NEEDS TO BE FIXED

        # Create the object driver
        driver = self.driver

        # Open the following URL in the browser
        driver.get("https://magento.softwaretestingboard.com/")
        sleep(3)

        # [ You may have to switch to frame]
        # switch to frame 0
        #iframe = driver.find_element(By.XPATH, "/html/body/iframe")
        #iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(1)
        sleep(2)

        # ------------------

        # Selected item (Autumn Pullie)
        #autumn_pullie = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[10]/div/a')
        autumn_pullie = driver.find_element(By.XPATH, "//img[@alt='Autumn Pullie-M-Purple']")
        autumn_pullie.click()

        # Pick size (M)
        autumn_pullie_size = driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']")
        autumn_pullie_size.click()

        # Pick color (Purple)
        autumn_pullie_color = driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']")
        autumn_pullie_color.click()

        # Find and click add to cart button
        add_cart_button = driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']")
        add_cart_button.click()

        # Find and click the cart icon (Located top right of page)
        cart_button = driver.find_element(By.XPATH, "//a[@class='action showcart']")
        cart_button.click()

    #def test_to_checkout(self):

        # Find the “Proceed to Checkout” Button

        # Click on the “Proceed to Checkout” Button

        # Assert the “Order summary” with assertEqual, Your shopping cart should show the dress selected by you


    # Finally close the browser
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


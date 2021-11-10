import time

import pytest
from selenium import webdriver

from PageObjects.Confirmation import ConfirmationPage
from PageObjects.HomePage import HomePage
from PageObjects.ShopPage import ShopPage
from Utilities.Base import Base


class Test(Base):

    def test_check_out_item(self):
        log = self.logging()
        products = ['blackberry', 'Iphone X']
        log.info(products)
        log.info("Homepage")
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        log.info("ShopPage")
        item_list = ShopPage(self.driver)
        shop_list = item_list.get_products_list()
        for product in shop_list:
            if product.find_element_by_xpath("div/h4/a").text.lower() in products:
                product.find_element_by_xpath("div/button").click()
        add_cart = ShopPage(self.driver)
        add_cart.add_cart().click()
        cart = ShopPage(self.driver)
        cart_products = cart.cart_products()
        log.info(cart_products)
        for product in cart_products:
            assert product.text.lower() in products
        log.info("Confirmation Page")
        check_out = ConfirmationPage(self.driver)
        check_out.check_out().click()
        country = ConfirmationPage(self.driver)
        country.country().clear()
        log.info("Country entered as India")
        country.country().send_keys("India")
        countries_list = self.driver.find_elements_by_xpath("//div[@class = 'suggestions']/ul/li/a")
        log.info(countries_list)
        for value in countries_list:
            if value.text == "India":
                value.click()
        check_box = ConfirmationPage(self.driver)
        check_box.check_box().click()
        purchase = ConfirmationPage(self.driver)
        purchase.purchase().click()
        success_text = ConfirmationPage(self.driver)
        log.info(success_text.success_text().text)
        assert 'Success' in success_text.success_text().text
        self.driver.get_screenshot_as_file("Sucess.png")




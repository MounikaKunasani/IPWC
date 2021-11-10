from selenium.webdriver.common.by import By


class ConfirmationPage:
    check = (By.XPATH, "//button[@class = 'btn btn-success']")
    country_id = (By.ID, "country")
    countries = (By.XPATH, "//div[@class = 'suggestions']/ul/li/a")
    box = (By.XPATH, "//div[@class = 'checkbox checkbox-primary']")
    purchase_button = (By.XPATH, "//input[@value = 'Purchase']")
    text = (By.XPATH, "//div[@class = 'alert alert-success alert-dismissible']")

    def __init__(self, driver):
        self.driver = driver

    def check_out(self):
        return self.driver.find_element(*ConfirmationPage.check)

    def country(self):
        return self.driver.find_element(*ConfirmationPage.country_id)

    def countries_list(self):
        return self.driver.find_element(*ConfirmationPage.countries)

    def check_box(self):
        return self.driver.find_element(*ConfirmationPage.box)

    def purchase(self):
        return self.driver.find_element(*ConfirmationPage.purchase_button)

    def success_text(self):
        return self.driver.find_element(*ConfirmationPage.text)
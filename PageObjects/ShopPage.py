from selenium.webdriver.common.by import By


class ShopPage:
    products_list = (By.XPATH, "//div[@class = 'card h-100']")
    product = (By.XPATH, "div/h4/a")
    check_out = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")
    products = (By.XPATH, "//div[@class = 'media']/div/h4")

    def __init__(self, driver):
        self.driver = driver

    def get_products_list(self):
        return self.driver.find_elements(*ShopPage.products_list)

    def desired_product(self):
        return self.driver.find_element(*ShopPage.product)

    def add_cart(self):
        return self.driver.find_element(*ShopPage.check_out)

    def cart_products(self):
        return self.driver.find_elements(*ShopPage.products)
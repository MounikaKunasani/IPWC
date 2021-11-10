from selenium.webdriver.common.by import By


class HomePage:

    shop = (By.LINK_TEXT, "Shop")
    text = (By.XPATH, "//div[@class = 'jumbotron']/h1")
    name = (By.XPATH, "//input[@name ='name']")
    email = (By.XPATH, "//input[@name ='email']")
    password = (By.CSS_SELECTOR, "input[id='exampleInputPassword1']")
    check_box = (By.XPATH, "//input[@id = 'exampleCheck1']")
    dropdown = (By.CSS_SELECTOR, "select[class='form-control']")
    button = (By.XPATH, "//input[@class = 'btn btn-success']")
    message = (By.CSS_SELECTOR,"div[class = 'alert alert-success alert-dismissible']" )

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def get_text(self):
        return self.driver.find_element(*HomePage.text)

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_password(self):
        return self.driver.find_element(*HomePage.password)

    def click_check_box(self):
        return self.driver.find_element(*HomePage.check_box)

    def get_dropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def click_button(self):
        return self.driver.find_element(*HomePage.button)

    def get_message(self):
        return self.driver.find_element(*HomePage.message)

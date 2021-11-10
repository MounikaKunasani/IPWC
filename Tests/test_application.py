import time
import pytest
from selenium.webdriver.support.select import Select

from PageObjects.HoemPageData import HomepageData
from PageObjects.HomePage import HomePage
from Utilities.Base import Base


class Test1(Base):

    def test_home(self, getData):
        log = self.logging()
        home = HomePage(self.driver)
        log.info(home.get_text().text)
        log.info(f'Name {getData[0]}')
        home.get_name().send_keys(getData[0])
        log.info(f'Email {getData[1]}')
        home.get_email().send_keys(getData[1])
        log.info(f'Password {getData[2]}')
        home.get_password().send_keys(getData[2])
        home.click_check_box().click()
        log.info("Gender Dropdown")
        dropdown = Select(home.get_dropdown())
        log.info(f'Gender {getData[3]}')
        dropdown.select_by_visible_text(getData[3])
        home.click_button().click()
        message = home.get_message().text
        log.info(message)
        assert "success" in message
        time.sleep(2)
        self.driver.refresh()

    @pytest.fixture(params=HomepageData.home_page_data)
    def getData(self, request):
        return request.param


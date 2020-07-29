import yaml
from appium import webdriver

from page.po01_mainpagge import MainPage
from page.basepage import BasePage


class App(BasePage):
    with open("../datas/desired_caps.yaml", encoding='UTF-8') as f:
        caps = yaml.safe_load(f)["wework"]

    def start(self):
        if self.driver is None:
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        self.driver.quit()

    def goto_mainpage(self):
        return MainPage(self.driver)

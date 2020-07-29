import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 查找页面元素方法重构
    def find(self, locator):
        logging.info(f"find: {locator}")
        return self.driver.find_element(*locator)

    # 页面控件点击方法重构
    def find_and_click(self, locator):
        logging.info(f"find: {locator} and click")
        self.driver.find_element(*locator).click()

    # 页面控件输入方法重构
    def find_and_sendkeys(self, locator, text):
        logging.info(f"find: {locator} and send_keys: {text}")
        self.driver.find_element(*locator).send_keys(text)

    # 页面滚动查找方法重构
    def scroll_find(self, text):
        locator = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).\
                  scrollIntoView(new UiSelector().text("{text}").instance(0))'
        logging.info(f"scroll to find: {text}")
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, locator)

    # 页面滚动查找点击方法重构
    def scroll_and_click(self, text):
        locator = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).\
                  scrollIntoView(new UiSelector().text("{text}").instance(0))'
        logging.info(f"scroll to find: {text} and click")
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, locator).click()

    # 显示等待方法重构
    def wait_until(self, locator, time=10):
        logging.info(f"webdriver_wait: {locator}, timeout: {time}")
        ele = WebDriverWait(self.driver, time).until(lambda x: x.find_element(*locator))
        return ele

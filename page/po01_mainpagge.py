import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.po02_contact import Contact
from page.basepage import BasePage


class MainPage(BasePage):
    with open("../datas/page_yaml/po01_mainpage.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 切换联系人页面
    def goto_contact(self):
        contact_ele = (MobileBy.XPATH, self.yaml_read["contact_ele"])
        self.find_and_click(contact_ele)
        return Contact(self.driver)

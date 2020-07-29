import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.po06_perinfomenu import PerinfoMenu
from page.basepage import BasePage


class PerInfo(BasePage):
    """
    个人信息页面PO
    """
    with open("../datas/page_yaml/po05_perinfo.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    def perinfo_menu(self):
        perinfomenu_ele = (MobileBy.XPATH, self.yaml_read["perinfomenu_ele"])
        # 点击设置省略号
        self.find_and_click(perinfomenu_ele)
        return PerinfoMenu(self.driver)

    # 返回上一页
    def page_back(self):
        page_back_ele = (MobileBy.XPATH, self.yaml_read["page_back_ele"])
        self.find_and_click(page_back_ele)
        from page.po02_contact import Contact
        return Contact(self.driver)

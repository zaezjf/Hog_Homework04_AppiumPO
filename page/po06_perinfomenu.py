from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy

from page.po07_editmember import EditMem
from page.basepage import BasePage


class PerinfoMenu(BasePage):
    """
    个人信息菜单页面PO
    """
    with open("../datas/page_yaml/po06_perinfomenu.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 点击“编辑成员”选项
    def goto_memedit(self):
        edit_mem_ele = (MobileBy.XPATH, self.yaml_read["edit_mem_ele"])
        self.find_and_click(edit_mem_ele)
        return EditMem(self.driver)

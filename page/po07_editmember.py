import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.basepage import BasePage


class EditMem(BasePage):
    """
    成员编辑页面PO
    """
    with open("../datas/page_yaml/po07_editmember.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 点击删除成员
    def del_member(self):
        # delete_mem_ele = (MobileBy.XPATH, self.yaml_read["delet_mem_ele"])
        # self.find_and_click(delete_mem_ele)
        self.scroll_and_click(self.yaml_read["delete_mem"])
        delete_confirm = (MobileBy.XPATH, self.yaml_read["delete_confirm"])
        self.find_and_click(delete_confirm)
        from page.po02_contact import Contact
        return Contact(self.driver)

    # 返回上一页
    def page_back(self):
        page_back_ele = (MobileBy.ID, self.yaml_read["page_back_ele"])
        self.find_and_click(page_back_ele)
        from page.po06_perinfomenu import PerinfoMenu
        return PerinfoMenu(self.driver)

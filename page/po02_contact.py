import yaml
from appium.webdriver.common.mobileby import MobileBy

from page.po03_addmember import AddMember
from page.po03_searchmember import SearchMember
from page.po05_perinfo import PerInfo
from page.basepage import BasePage


class Contact(BasePage):
    with open("../datas/page_yaml/po02_contact.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 点击联系人页面“添加成员”控件
    def goto_addmember(self):
        self.scroll_and_click(self.yaml_read["addmember_ele"])
        return AddMember(self.driver)

    # 选择联系人页面name成员
    def goto_perinfo(self, name):
        # 选择要删除的联系人
        self.scroll_and_click(name)
        return PerInfo(self.driver)

    # 点击“搜索”按钮
    def goto_search(self):
        search_ele = (MobileBy.XPATH, self.yaml_read["search_ele"])
        self.find_and_click(search_ele)
        return SearchMember(self.driver)
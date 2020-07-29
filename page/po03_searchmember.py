import yaml
from appium.webdriver.common.mobileby import MobileBy


from page.po05_perinfo import PerInfo
from page.basepage import BasePage


class SearchMember(BasePage):
    with open("../datas/page_yaml/po03_searchmember.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 点击搜索框，输入搜索成员名
    def search_member(self, search_text):
        input_search_ele = (MobileBy.XPATH, self.yaml_read["input_search_ele"])
        self.find_and_sendkeys(input_search_ele, search_text)
        try:
            member_ele = (MobileBy.XPATH, self.yaml_read["member_ele"]+f"[@text={search_text}]")
            self.find_and_click(member_ele)
            return PerInfo(self.driver)
        except:
            return "未找到成员"

    # 返回上一页
    def page_back(self):
        page_back_ele = (MobileBy.ID, self.yaml_read["page_back_ele"])
        self.find_and_click(page_back_ele)
        from page.po02_contact import Contact
        return Contact(self.driver)

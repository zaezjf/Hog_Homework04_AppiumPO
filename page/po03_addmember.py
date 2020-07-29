import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.po04_manualadd import ManualAdd
from page.basepage import BasePage


class AddMember(BasePage):
    """
    添加成员页面PO
    """
    with open("../datas/page_yaml/po03_addmember.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 点击 "手动输入添加"跳转到添加成员手动编辑页
    def goto_manualadd(self):
        manualadd_ele = (MobileBy.XPATH, self.yaml_read["manualadd_ele"])
        self.find_and_click(manualadd_ele)
        return ManualAdd(self.driver)

    # 返回上一页
    def page_back(self):
        page_back_ele = (MobileBy.ID, self.yaml_read["page_back_ele"])
        self.find_and_click(page_back_ele)
        from Appium.PO.po02_contact import Contact
        return Contact(self.driver)

    # 获取添加成功后的toast提示文本
    def get_toast(self):
        toast_ele = (MobileBy.XPATH, self.yaml_read["toast_ele"])
        result = self.wait_until(toast_ele).text
        return result

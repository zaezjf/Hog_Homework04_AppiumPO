import yaml
from appium.webdriver.common.mobileby import MobileBy
from page.basepage import BasePage


class ManualAdd(BasePage):
    """
    手动输入添加成员页面PO
    """
    with open("../datas/page_yaml/po04_manualadd.yaml", encoding='UTF-8') as f:
        yaml_read = yaml.safe_load(f)

    # 输入姓名
    def set_name(self, name):
        input_name_ele = (MobileBy.XPATH, self.yaml_read["input_name_ele"])
        self.find_and_sendkeys(input_name_ele, name)
        return self

    # 选择性别
    def set_gender(self, gender):
        set_gender_ele = (MobileBy.XPATH, self.yaml_read["set_gender_ele"])
        self.find_and_click(set_gender_ele)
        if gender == "男":
            man_ele = (MobileBy.XPATH, self.yaml_read["man_ele"])
            self.find_and_click(man_ele)
        else:
            woman_ele = (MobileBy.XPATH, self.yaml_read["woman_ele"])
            self.find_and_click(woman_ele)
        return self

    # 输入手机号
    def set_phone(self, phone):
        input_phone_ele = (MobileBy.XPATH, self.yaml_read["input_phone_ele"])
        self.find_and_sendkeys(input_phone_ele, phone)
        return self

    # 保存
    def click_save(self):
        save_ele = (MobileBy.XPATH, self.yaml_read["save_ele"])
        self.find_and_click(save_ele)
        from page.po03_addmember import AddMember
        return AddMember(self.driver)

    # 左上角返回按钮
    def page_back(self):
        page_back_ele = (MobileBy.ID, self.yaml_read["page_back_ele"])
        self.find_and_click(page_back_ele)
        from page.po03_addmember import AddMember
        return AddMember(self.driver)

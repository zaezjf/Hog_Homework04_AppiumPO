import pytest
import yaml
from page.po00_app import App


class TestContact:
    with open("../datas/member_list.yaml", encoding="UTF-8") as f:
        add_contact_datas = yaml.safe_load(f)
    with open("../datas/member_name.yaml", encoding="UTF-8") as f:
        del_contact_datas = yaml.safe_load(f)

    # 初始化APP
    def setup_class(self):
        self.app_start = App().start()

    # 退出driver
    def teardown_class(self):
        self.app_start.stop()

    # 进入通讯录页面
    def setup(self):
        self.contact = self.app_start.goto_mainpage().goto_contact()

    # 返回到通讯录页面
    def teardown(self):
        self.app_start.driver.back()

    # 用例1：添加成员
    @pytest.mark.parametrize("name, gender, phone", add_contact_datas)
    def test_add_contact(self, name, gender, phone):
        # 步骤1：点击通讯录页面的“添加成员”按钮选项
        step1 = self.contact.goto_addmember()
        # 步骤2：选择页面的“手动输入添加”选项，进入添加成员编辑页面
        step2 = step1.goto_manualadd()
        # 步骤3：输入姓名
        step3 = step2.set_name(name)
        # 步骤4：设置性别
        step4 = step3.set_gender(gender)
        # 步骤5：输入手机号
        step5 = step4.set_phone(phone)
        # 步骤6：点击"保存"并确认
        step6 = step5.click_save()
        # 步骤7：保存成功后，返回添加成员页面，获取toast
        result = step6.get_toast()
        assert "添加成功" in result

    # 用例2：删除成员
    @pytest.mark.parametrize("name", del_contact_datas)
    def test_del_contact(self, name):
        # 步骤1：通讯录页面选择需要删除的成员
        step1 = self.contact.goto_perinfo(name)
        # 步骤2：选择个人信息页右上角菜单按钮
        step2 = step1.perinfo_menu()
        # 步骤3：点击个人信息菜单页的“编辑成员”选项
        step3 = step2.goto_memedit()
        # 步骤4：点击“删除成员”选项
        step4 = step3.del_member()
        # 步骤5：判断是否删除成功
        result = step4.goto_search().search_member(name)
        assert "未找到" in result

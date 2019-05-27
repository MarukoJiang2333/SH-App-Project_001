import allure
import pytest


class Test002:

    @allure.step(title="这是测试方法一")
    def test_001(self):
        print("------test001------")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是测试方法二")
    def test_002(self):
        print("-----test002-------")

        with open("./Scripts\\abc.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)
        assert False
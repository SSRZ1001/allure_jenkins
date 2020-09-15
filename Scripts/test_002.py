import allure


class Test_001:
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('第一步')
    def test_01(self):
        print('test001')

    @allure.severity(allure.severity_level.NORMAL)
    def test_02(self):
        print('test002')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_03(self):
        print('test003')
        assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_04(self):
        print('test004')

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_05(self):
        print('test005')

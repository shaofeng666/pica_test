# from util.modules import ddt
# from util.gettestdata import get_testcase
# from config import root_path
# from util.test_star_end import TestStarEnd
# from bussinses.login_page import Login_test
# from util import log
#
# case_path = root_path + '\\data\\case.xlsx'
# casedata = get_testcase(case_path, 1, '登录')
#
#
# @ddt.ddt
# class Testlogin(TestStarEnd):
#     @ddt.data(*casedata)
#     def test_login1(self, casedata):
#         self.logs = log.log_message('登陆测试')
#         self.name = casedata['username']
#         self.pwd = casedata['pwd']
#         self.suc = casedata['suc']
#         self.assert_value = casedata['assert']
#         self.re_data = Login_test(self.driver).login(self.name, self.pwd, self.suc)
#         self.logs.logger.info('断言预期结果:[%s]是否等于实际结果:[%s]' % (self.assert_value, self.re_data))
#         # self.imgs.append(self.driver.add_img()) #截图
#         self.assertEqual(self.re_data, self.assert_value)
#
#
# if __name__ == '__main__':
#     Testlogin().test_login1()
#     print(casedata)
#

# # -*- coding: utf-8 -*-
# # @Date    : 2018-12-15 20:48:37
# # @Author  : Victor
# from bussinses.manage_patient.add_patient_page import add_patient_obj
# from bussinses.manage_patient.del_patient_page import del_patient_obj
# from bussinses.storage_login import storage_login
# from util.modules import ddt
# from util.gettestdata import get_testcase
# from config import root_path
# from util.test_star_end import TestStarEnd
# from util import log
#
# case_path = root_path + '\\data\\case.xlsx'
# del_patient_data = get_testcase(case_path, 2, '删除病人')
# add_patient_data = get_testcase(case_path, 2, '添加病人')
#
#
# @ddt.ddt
# class add_patient(TestStarEnd):
#     def test_add_patient(self):  # 增加居民
#         storage_login(self.driver)
#         add_patient_obj(self.driver).add_patient('15607241351', '2222', '确认', '关闭')
#
#         # add_patient_obj(self.driver).add_patient('15607241351','2222','取消','')
#         # add_patient_obj(self.driver).add_patient('15607241351','2222','确认','')
#
#     @ddt.data(*del_patient_data)
#     def test_del_patient(self, del_patient_data):  # 删除居民
#         storage_login(self.driver)
#         moblie = del_patient_data['moblie']
#         is_confrim = del_patient_data['is_confrim']
#         assert_value = del_patient_data['assert']
#         print(moblie, is_confrim, assert_value)
#         re_data = del_patient_obj(self.driver).del_patient(moblie, is_confrim, self.imgs)
#         self.logs.logger.info('断言预期结果:[%s]是否等于实际结果:[%s]' % (assert_value, re_data))
#         self.assertEqual(re_data, assert_value)
#
#
# if __name__ == '__main__':
#     # add_patient().test_add_patient()
#     add_patient().test_del_patient()

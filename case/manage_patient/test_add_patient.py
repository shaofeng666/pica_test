# -*- coding: utf-8 -*-
# @Date    : 2018-12-15 20:48:37
# @Author  : Victor
from bussinses.manage_patient.add_patient_page import add_patient_obj
from bussinses.manage_patient.del_patient_page import del_patient_obj
from bussinses.storage_login import storage_login
from util.modules import ddt
from util.gettestdata import get_testcase
from config import root_path
from util.test_star_end import TestStarEnd
from util import log

case_path = root_path + '\\data\\case.xlsx'
add_patient_data = get_testcase(case_path, 2, '添加病人')


@ddt.ddt
class add_patient(TestStarEnd):
    @ddt.data(*add_patient_data)
    def test_add_patient(self, add_patient_data):  # 增加居民
        self.log = log.log_message('添加居民')
        moblie = add_patient_data['moblie']
        name = add_patient_data['name']
        is_confrim = add_patient_data['is_confrim']
        is_continue = add_patient_data['is_continue']
        assert_value = add_patient_data['assert']
        address = add_patient_data['address']
        storage_login(self.driver)
        re_data = add_patient_obj(self.driver, self.log).add_patient(moblie, name, is_confrim, is_continue, address)
        # self.logs.logger.info('断言预期结果:[%s]是否等于实际结果:[%s]' % (assert_value, re_data))
        # self.assertEqual(re_data, assert_value)

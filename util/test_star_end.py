import unittest
from util.selse_feng import CreateDriver
from util import log


class TestStarEnd(unittest.TestCase):
    '''
    unittest 公共的setUp 与tearDowm
    '''

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.driver = CreateDriver(self.imgs)
        self.logs = log.log_message('初始化')
        self.logs.logger.info('启动')

    def tearDown(self):
        # self.imgs.append(self.driver.add_img())
        self.driver.quit()

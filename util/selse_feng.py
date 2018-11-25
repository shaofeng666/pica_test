from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from util import log
from config import root_path


class CreateDriver():
    def __init__(self, brower):  # 初始化浏览器
        if brower == 'firefox' or brower == 'Firefox' or brower == 'f' or brower == 'F':
            deriver = webdriver.Firefox(root_path + "\\browser_driver\\geckodriver.exe")
        elif brower == 'Ie' or brower == 'ie' or brower == 'i' or brower == 'I':
            deriver = webdriver.Ie(root_path + "\\browser_driver\\IEDriverServer.exe")
        elif brower == 'Chrome' or brower == 'chrome' or brower == 'Ch' or brower == 'ch':
            deriver = webdriver.Chrome(root_path + "\\browser_driver\\chromedriver.exe")
        elif brower == 'PhantomJS' or brower == 'phantomjs' or brower == 'ph' or brower == 'phjs':
            deriver = webdriver.PhantomJS()
        elif brower == 'Edge' or brower == 'edge' or brower == 'Ed' or brower == 'ed':
            deriver = webdriver.Edge()
        elif brower == 'Opera' or brower == 'opera' or brower == 'op' or brower == 'OP':
            deriver = webdriver.Opera()
        elif brower == 'Safari' or brower == 'safari' or brower == 'sa' or brower == 'saf':
            deriver = webdriver.Safari()
        else:
            raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
        self.driver = deriver
        self.logs = log.log_message("页面对象")

    def element(self, fangfa, dingwei):  # 定位
        if fangfa == 'id':
            element = self.driver.find_element_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def elements(self, fangfa, dingwei):  # 组定位
        if fangfa == 'id':
            element = self.driver.find_elements_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_elements_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_elements_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_elements_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_elements_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_elements_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_elements_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def element_wait(self, fangfa, dingwei, wati=10):  # 等待
        if fangfa == "id":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.ID, dingwei)))
        elif fangfa == "name":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.NAME, dingwei)))
        elif fangfa == "class":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
        elif fangfa == "link_text":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
        elif fangfa == "xpath":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
        elif fangfa == "css":
            WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    def open(self, url):  # 打开网页
        self.logs.logger.info('打开网页[%s]' % url)
        self.driver.get(url)

    def make_maxwindow(self):  # 最大化浏览器
        self.logs.logger.info('最大化浏览器')
        self.driver.maximize_window()

    def set_winsize(self, wide, hight):  # 设置窗口
        self.logs.logger.info('设置窗口尺寸宽[%s]高[%s]' % (wide, hight))
        self.driver.set_window_size(wide, hight)

    def send_key(self, fangfa, dingwei, text):  # 发送内容
        self.logs.logger.info('在[%s]为[%s]的元素内输入[%s]' % (fangfa, dingwei, text))
        # self.element(fangfa, dingwei)
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()
        e1.send_keys(text)

    def clear_send_key(self, fangfa, dingwei, text):  # 清空并发送内容
        # self.element(fangfa, dingwei)
        self.logs.logger.info('点击[%s]为[%s]的元素清空内容，并输入[%s]' % (fangfa, dingwei, text))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()
        e1.clear()
        e1.send_keys(text)

    def clear(self, fangfa, dingwei):  # 清空
        self.logs.logger.info('点击[%s]为[%s]的元素并清空内容' % (fangfa, dingwei))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()
        e1.clear()

    def click(self, fangfa, dingwei):  # 单击
        self.logs.logger.info('点击[%s]为[%s]的元素' % (fangfa, dingwei))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.click()

    def right_click(self, fangfa, dingwei):  # 右击
        self.logs.logger.info('右键点击[%s]为[%s]的元素' % (fangfa, dingwei))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    def move_element(self, fangfa, dingwei):  # 移动到
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).move_to_element(e1).perform()

    def double_click(self, dingwei, fangfa):  # 双击
        self.logs.logger.info('双击[%s]为[%s]的元素' % (fangfa, dingwei))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):  # 从e1到e2
        self.element_wait(fangfa1, e1)
        eme1 = self.element(fangfa1, e1)
        self.element_wait(fangfa2, e2)
        eme2 = self.element(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):  # 点击文字
        self.logs.logger.info("点击a标签：[%s]" % text)
        self.driver.find_element_by_link_text(text).click()

    def close(self):  # 关闭
        self.logs.logger.info('关闭浏览器当前窗口')
        self.driver.close()

    def quit(self):  # 退出
        self.logs.logger.info('关闭浏览器')
        self.driver.quit()

    def sublimit(self, fangfa, dingwei):  # 提交
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        e1.sublimit()

    def f5(self):  # 刷新
        self.logs.logger.info('刷新')
        self.driver.refresh()

    def js(self, sprit):  # 执行js
        self.logs.logger.info('执行js%s' % sprit)
        self.driver.execute_script(sprit)

    #     "document.getElementById('id').value='内容'"

    def get_attribute(self, fangfa, dingwei, attribute):
        e1 = self.element(fangfa, dingwei)
        return e1.get_attribute(attribute)

    def get_text(self, fangfa, dingwei):  # 获取文本值
        self.logs.logger.info('获取[%s]为[%s]元素的文本值' % (fangfa, dingwei))
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.text

    def get_is_dis(self, fangfa, dingwei):
        self.element_wait(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.is_displayed()

    def get_title(self, fangfa, dingwei):  # 获取title
        self.logs.logger.info('获取[%s]为[%s]的title' % (fangfa, dingwei))
        return self.driver.title

    def get_screen(self, file_path):  # 截屏
        self.driver.get_screenshot_as_file(file_path)

    def add_img(self):
        self.logs.logger.info('获取当前窗口的截图保存为一个base64编码的字符串。')
        return self.driver.get_screenshot_as_base64()  # 获取当前窗口的截图保存为一个base64编码的字符串。

    def wait(self, fangfa, dingwei):  # 等待
        self.logs.logger.info('隐性等待')  # 在一段时间内判断网页是否加载完成
        self.driver.implicitly_wait((fangfa, dingwei))

    def accpet(self):  # 接受警告框
        self.logs.logger.info('接受警告框')
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, fangfa, dingwei):  # 切换到iframe表单
        self.logs.logger.info('切换到iframe表单')
        self.element_wait(fangfa, dingwei)
        if1 = self.element(fangfa, dingwei)
        self.driver.switch_to.frame(if1)

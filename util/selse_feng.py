from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from util import log
from config import root_path
from time import sleep
from config import brower


class CreateDriver(object):
    def __init__(self,imgs):  # 初始化浏览器
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
            raise NameError("-CreateDriver()对象只能传入：firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari;请确认%s是否合法" % brower)
        self.imgs=imgs
        self.driver = deriver
        self.logs = log.log_message("页面对象")

    def element(self, fangfa, dingwei):  # 定位
        if fangfa == 'id':
            element = self.driver.find_element_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text" or fangfa == "a" or fangfa == "A":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError(
                "-element()方法元素定位方式只包含：'id','name','class','link_text','xpath','css','tag';请确认%s是否合法" % fangfa)
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
            raise NameError(
                "-elements()组定位方式只包含:'id','name','class','link_text','xpath','css','tag';请确认%s是否合法" % fangfa)
        return element

    def element_wait(self, fangfa, dingwei, wati=3):  # 等待
        try:
            if fangfa == "id":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.ID, dingwei)))
            elif fangfa == "name":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.NAME, dingwei)))
            elif fangfa == "class":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
            elif fangfa == "link_text" or fangfa == "a" or fangfa == "A":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
            elif fangfa == "xpath":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
            elif fangfa == "css":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
            else:
                raise NameError(
                    "-element_wait()等待定位方式入参只包含：'id','name','class','link_text','xpath','css'.;请确认%s是否合法" % fangfa)
            return element
        except TimeoutException as e:
            sleep(1)  # 等待1秒后重试
            if fangfa == "id":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.ID, dingwei)))
            elif fangfa == "name":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.NAME, dingwei)))
            elif fangfa == "class":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
            elif fangfa == "link_text" or fangfa == "a" or fangfa == "A":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
            elif fangfa == "xpath":
                element = WebDriverWait(self.driver, wati, 1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
            elif fangfa == "css":
                element = WebDriverWait(self.driver, wati, 1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
            else:
                raise NameError(
                    "-element_wait()等待定位方式入参只包含：'id','name','class','link_text','xpath','css'.;请确认%s是否合法" % fangfa)
            return element
        except Exception as e:
            self.logs.logger.error('element_wait()方法执行失败，原因：%s' % e)


    def open(self, url):  # 打开网页并最大化浏览器
        self.logs.logger.info('打开网页[%s]' % url)
        self.driver.maximize_window()
        self.driver.get(url)

    def make_maxwindow(self):  # 最大化浏览器
        self.logs.logger.info('最大化浏览器')
        self.driver.maximize_window()

    def set_winsize(self, wide, hight):  # 设置窗口
        self.driver.set_window_size(wide, hight)
        self.logs.logger.info('设置窗口尺寸宽[%s]高[%s]' % (wide, hight))

    def send_key(self, fangfa, dingwei, text):  # 发送内容
        try:
            e1 = self.element_wait(fangfa, dingwei)
            e1.click()
            e1.send_keys(text)
            self.imgs.append(self.driver.get_screenshot_as_base64())
            self.logs.logger.info('获取当前窗口的截图保存为一个base64编码的字符串。')
            self.logs.logger.info('在[%s]为[%s]的元素内输入[%s]' % (fangfa, dingwei, text))
        except TimeoutException as e:
            self.logs.logger.error('send_key()方法执行失败，原因TimeoutException:%s' % e)
        except Exception as e:
            self.logs.logger.error('用例执行失败，原因：%s' % e)

    def clear_send_key(self, fangfa, dingwei, text):  # 清空并发送内容
        try:
            e1 = self.element_wait(fangfa, dingwei)
            e1.click()
            sleep(1)
            e1.clear()
            e1.send_keys(text)
            self.logs.logger.info('点击[%s]为[%s]的元素清空内容，并输入[%s]' % (fangfa, dingwei, text))
            self.imgs.append(self.driver.get_screenshot_as_base64())
            self.logs.logger.info('获取当前窗口的截图保存为一个base64编码的字符串。')
        except TimeoutException as e:
            self.logs.logger.error('clear_send_key()方法执行失败，原因TimeoutException:%s' % e)
        except Exception as e:
            self.logs.logger.error('用例执行失败，原因：%s' % e)

    def clear(self, fangfa, dingwei):  # 清空
        try:
            self.logs.logger.info('点击[%s]为[%s]的元素并清空内容' % (fangfa, dingwei))
            e1 = self.element_wait(fangfa, dingwei)
            e1.click()
            e1.clear()
        except TimeoutException as e:
            self.logs.logger.error('clear()方法执行失败，原因TimeoutException:%s' % e)
        except Exception as e:
            self.logs.logger.error('用例执行失败，原因：%s' % e)

    def click(self, fangfa, dingwei):  # 单击
        try:
            e1 = self.element_wait(fangfa, dingwei)
            e1.click()
            self.logs.logger.info('点击[%s]为[%s]的元素' % (fangfa, dingwei))
        except TimeoutException as e:
            self.logs.logger.error('click()方法执行失败，原因TimeoutException:%s' % e)
        except Exception as e:
            self.logs.logger.error('click()执行失败，原因：%s' % e)

    def right_click(self, fangfa, dingwei):  # 右击
        self.logs.logger.info('右键点击[%s]为[%s]的元素' % (fangfa, dingwei))
        e1 = self.element_wait(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    def move_element(self, fangfa, dingwei):  # 移动到
        self.logs.logger.info('进入move_element()方法')
        e1 = self.element_wait(fangfa, dingwei)
        ActionChains(self.driver).move_to_element(e1).perform()
        self.logs.logger.info('鼠标移动到[%s]为[%s]的元素' % (fangfa, dingwei))


    def double_click(self, dingwei, fangfa):  # 双击
        self.logs.logger.info('双击[%s]为[%s]的元素' % (fangfa, dingwei))
        e1 = self.element_wait(fangfa, dingwei)
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):  # 从e1到e2
        eme1 = self.element_wait(fangfa1, e1)
        eme2 = self.element_wait(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(eme1, eme2).perform()

    def click_text(self, text):  # 点击超链接
        self.logs.logger.info("点击a标签：[%s]" % text)
        e1 = self.element_wait('link_text', text)
        e1.click()

    def close(self):  # 关闭
        self.logs.logger.info('关闭浏览器当前窗口')
        self.driver.close()

    def quit(self):  # 退出
        self.logs.logger.info('关闭浏览器\n')
        self.driver.quit()

    def sublimit(self, fangfa, dingwei):  # 提交
        e1 = self.element_wait(fangfa, dingwei)
        e1.sublimit()

    def f5(self):  # 刷新
        self.logs.logger.info('刷新')
        self.driver.refresh()

    def js(self, sprit):  # 执行js
        sleep(2)
        self.logs.logger.info('执行js%s' % sprit)
        self.driver.execute_script(sprit)

    def get_attribute(self, fangfa, dingwei, attribute):
        e1 = self.element_wait(fangfa, dingwei)
        return e1.get_attribute(attribute)

    def get_text(self, fangfa, dingwei):  # 获取文本值
        try:
            e1 = self.element_wait(fangfa, dingwei)
            if e1.text == None or e1.text == '':  # 如果文本值为null，则等待3秒后重新获取
                sleep(3)
                e2 = self.element_wait(fangfa, dingwei)
                self.logs.logger.info('-重试-获取[%s]为[%s]元素的文本值,return:[%s]' % (fangfa, dingwei, e2.text))
                self.imgs.append(self.driver.get_screenshot_as_base64())
                self.logs.logger.info('获取当前窗口的截图保存为一个base64编码的字符串。')
                return e2.text
            else:  # 不为null 直接return
                self.logs.logger.info('获取[%s]为[%s]元素的文本值,return:[%s]' % (fangfa, dingwei, e1.text))
                self.imgs.append(self.driver.get_screenshot_as_base64())
                self.logs.logger.info('获取当前窗口的截图保存为一个base64编码的字符串。')
                return e1.text
        except TimeoutException as e:
            self.logs.logger.error('get_text()方法执行失败，原因:TimeoutException:%s' % e)
        except Exception as e:
            self.logs.logger.error('用例执行失败，原因：%s' % e)

    def get_is_dis(self, fangfa, dingwei):
        e1 = self.element_wait(fangfa, dingwei)
        return e1.is_displayed()

    def get_title(self):  # 获取title
        title = self.driver.title
        self.logs.logger.info('获取当前页面的title;return:[%s]')
        return title

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
        if1 = self.element_wait(fangfa, dingwei)
        self.driver.switch_to.frame(if1)

    def selenium_driver(self):  # 返回selenium的driver，方便调用原有的方法。例如get_cookies
        return self.driver

from selenium import webdriver
import time
import unittest
class QQ(unittest.TestCase):
    def setUp(self):
        self.wb=webdriver.Firefox()
        self.wb.get("https://mail.qq.com/")
        time.sleep(5)
    #正常登录
    def test_case1(self):
        self.wb.switch_to.frame("login_frame")
        time.sleep(2)
        self.wb.find_element_by_id("u").send_keys(1947441766)
        time.sleep(2)
        self.wb.find_element_by_id("p").send_keys("RZN930529")
        time.sleep(2)
        self.wb.find_element_by_id("login_button").click()
        self.wb.switch_to.default_content()
        time.sleep(2)
        a=self.wb.find_element_by_id("composebtn").text
        self.assertEqual(a,"写信",msg="登录失败")
        time.sleep(5)

    def tearDown(self):
        self.wb.close()
        self.wb.quit()

if __name__ == '__main__':
    unittest.main()
from selenium import webdriver
import time
wb=webdriver.Firefox()
wb.get("https://www.baidu.com")
wb.maximize_window()
time.sleep(2)
picture_time=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
print(picture_time)
try:
    picture_url=wb.get_screenshot_as_file("H:\\课件\\ceshi\\"+picture_time+".png")
    print("%s：截图成功"%picture_url)
except BaseException as msg:
    print(msg)
wb.quit()
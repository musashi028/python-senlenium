import time
import datetime
from PIL import Image
import easyocr
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
arr = (
    '张三','李四')
driver = webdriver.Chrome()
#reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
#result = reader.readtext(r'C:\Users\musaxi\Desktop\1111.png')
#print(result)
driver.get('http://test.com')
time.sleep(3)  # 强制等待3秒再执行下一步
driver.find_element_by_id("username").send_keys('username')
driver.find_element_by_id("password").send_keys('password')
image_=driver.find_element_by_id("captchaid")


time.sleep(10) #输入密码需要时间
driver.find_element_by_name("submit1").submit()
flag=True
def isElementExist(driver, param):
    flag = True
    browser = driver
    try:
        browser.find_element_by_xpath(param)
        return flag
    except:
        flag = False
        return flag


for tp in arr:
    driver.find_element_by_id("email_serach").send_keys(tp)
    driver.find_element_by_id("search_link").click()  # 页面加载完就执行
    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "load-simple-dialog")))
        if isElementExist(driver, "//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[2]"):
            value1 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[2]").text
            value2 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[3]").text
            value3 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[4]").text
            value4 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[5]").text
            value5 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[6]").text
            value6 = driver.find_element_by_xpath("//*[@id='load-simple-dialog']/table/tbody[2]/tr[2]/td[7]").text
            print(value1 + "," + value2 + "," + value3 + "," + value4 + "," + value5 + "," + value6)

        elif isElementExist(driver, "//*[@id='load-simple-dialog']/table/tbody/tr[2]/td[1]/a"):
                print(tp+" 有重名！")
        else:
            print(tp + " 员工没找到！")
    finally:
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/a").click()
            flag=False
    if flag:
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/a").click()
        flag=True
    driver.find_element_by_id("email_serach").clear()  # 清空数据

import time
import pandas as pd
import os
import sys
import xlrd
import datetime
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
def getNum(num,reason,driver):
    if(num=='不能接种'):
        driver.find_element_by_xpath('/html/body/form/div/div[7]/div[1]/div/label[1]/input').click()
        driver.find_element_by_id('inputISVACCINATIONInfo').send_keys(reason)
    if(num=='未接种'):
        driver.find_element_by_xpath('/html/body/form/div/div[7]/div[1]/div/label[2]/input').click()
    if (num == '第一针'):
        driver.find_element_by_xpath('/html/body/form/div/div[7]/div[1]/div/label[3]/input').click()
    if (num == '第二针'):
        driver.find_element_by_xpath('/html/body/form/div/div[7]/div[1]/div/label[4]/input').click()
    if (num == '第三针'):
        driver.find_element_by_xpath('/html/body/form/div/div[7]/div[1]/div/label[5]/input').click()
if __name__=='__main__':
    xlsx = pd.read_excel('C:\\数据.xlsx',sheet_name='Sheet2',usecols='A:R')
    rows=xlsx.index.stop
    row=0
    while row<rows:
        name = xlsx.iloc[row, 3]
        id = xlsx.iloc[row, 4]
        type = xlsx.iloc[row, 5]
        provc = xlsx.iloc[row, 6]
        city = xlsx.iloc[row, 7]
        area = xlsx.iloc[row, 8]
        street = xlsx.iloc[row, 9]
        adds = xlsx.iloc[row, 10]
        highFlag = xlsx.iloc[row, 11]
        tempFlag = xlsx.iloc[row, 12]
        temp = xlsx.iloc[row, 13]
        greenFlag = xlsx.iloc[row, 14]
        COVID_NUM = xlsx.iloc[row, 15]
        reason = xlsx.iloc[row, 16]
        status = xlsx.iloc[row, 17]
        driver = webdriver.Chrome()
        driver.get(
            'https://test.com')
        time.sleep(1)  # 强制等待3秒再执行下一步
        driver.find_element_by_id("inputName").send_keys(name)
        driver.find_element_by_id("inputIdNo").send_keys(str(id))
        Select(driver.find_element_by_id("RYLBOption")).select_by_visible_text(type)
        driver.find_element_by_id("ProvinceOption").send_keys(provc)
        driver.find_element_by_id("CityOption").send_keys(city)
        driver.find_element_by_id("CountyOption").send_keys(area)
        driver.find_element_by_id("inputStreetInfo").send_keys(street)
        driver.find_element_by_id("inputJQDZInfo").send_keys(adds)
        if highFlag=='否':
            driver.find_element_by_xpath("/html/body/form/div/div[4]/div[3]/div/label[2]/input").click()
        else:
            driver.find_element_by_xpath("/html/body/form/div/div[4]/div[3]/div/label[1]/input").click()
        if tempFlag=='否':
            driver.find_element_by_xpath("/html/body/form/div/div[5]/div[1]/div/label[2]/input").click()
        else:
            driver.find_element_by_xpath("/html/body/form/div/div[5]/div[1]/div/label[1]/input").click()
        driver.find_element_by_name("inputTWInfo").send_keys(str(temp))
        if greenFlag=='是':
            driver.find_element_by_xpath('/html/body/form/div/div[6]/div/div/label[1]/input').click()
        else:
            driver.find_element_by_xpath('/html/body/form/div/div[6]/div/div/label[2]/input').click()
        getNum(COVID_NUM,reason,driver)
        Select(driver.find_element_by_id("ZGZTFGHOption")).select_by_visible_text(status)
        #driver.find_element_by_xpath("//*[@id='firstflag']/div[12]/button").click()
        print(name+"信息提交成功！")
        time.sleep(1)  # 强制等待3秒再执行下一步
        driver.close()
        row=row+1



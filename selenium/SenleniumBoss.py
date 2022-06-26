import time
import datetime

import selenium
from PIL import Image
#import easyocr
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
def isElementExist(driver, param):
    flag = True
    browser = driver
    try:
        browser.find_element_by_xpath(param)
        return flag
    except:
        flag = False
        return flag
driver.get('https://www.zhipin.com/web/boss/recommend')
# 强制等待20秒再执行下一步
time.sleep(15)
#跳转到推荐牛人
zhuanye_arr={"教育技术学","现代教育技术","现代信息技术教育","互联网广告设计","电脑艺术设计","信息与计算科学","计算数学及其应用软件","信息科学","电子信息科学与技术","微电子学","信息安全","网络与信息安全","计算机应用及安全管理","计算机与自动检测","网络工程","自动化","电子信息工程","通信工程","计算机科学与技术","电子科学与技术","信息工程","软件工程","微电子技术","应用电子技术","计算机及应用","计算机软件","计算机科学教育","电子与信息技术","计算机通信","计算机应用技术","计算机应用与维护","办公自动化设备运行与维修","通信技术","电子技术及微机应用","微型计算机及应用","办公自动化技术","计算机与信息管理","计算机辅助机械设计","计算机与邮政通信","信息处理与自动化","电器与电脑","数控技术及应用","网络技术与信息处理","计算机网络与软件应用","电子工程","计算机制图","电脑图文处理与制版","广告电脑制作","计算机网络技术","多媒体与网络技术","信息与多媒体技术","信息及通信网络应用技术","计算机网络工程与管理","计算机美术设计","计算机图形图像处理","计算机组装与维修","工厂计算机集中控制","计算机辅助设计","计算机控制技术","机电设备及微机应用","计算机系统维护技术","计算机辅助制造工艺","微电子控制技术","数据库应用与信息管理","计算机辅助设计与制造","信息管理与信息系统","经济信息管理与计算机应用","电子商务","企业信息计算机管理","数字媒体艺术","物联网工程","地图制图学与地理信息工程",}
jineng_arr={"python","selenium","自动化","fiddler","jmeter","postman","requests","unittest","pytest","接口","robot","rf","framework"}
buttons=driver.find_element_by_xpath("//*[@id='main']/div[1]/div/dl[2]/dt/a")
buttons.click()
try:
    time.sleep(3)  # 强制等待20秒再执行下一步
    #选择要找简历的岗位
    button_test1 = driver.find_element_by_xpath("//div[@id='recommendContent']/div/div/div[2]/div/i")
    button_test1.click()
    time.sleep(2)
    #找自动化测试人员
    button_test2 = driver.find_element_by_xpath("//div[@id='recommendContent']/div/div/div[2]/div[2]/div/ul/li[4]/span")
    button_test2.click()
    time.sleep(3)
    # 切入到iframe
    driver.switch_to_frame(0)
    #driver.switch_to.default_content() 切回到原来的iframe
    #获取人员简历表格内容
    listsize=driver.find_element_by_xpath("//div[@id='recommend-list']/div/ul")
    i=0
    j=0
    lists=listsize.find_elements_by_tag_name('li')
    print("获取了多少份简历："+str(lists.__len__()))
    for list in lists:
        if(i<int(lists.__len__())):
            totolscore=0
            i=i+1
            #打开人员简历信息
            button_test3 = driver.find_element_by_xpath("//div[@id='recommend-list']/div/ul/li["+ str(i) +"]/div/div")
            button_test3.click()
            time.sleep(2)
            #姓名
            name = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[1]/div[2]/div[1]/h2/div")
            print("name=" + name.text)
            #获取到岗时间
            daogang = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[1]/div[2]/div[1]/div/span[4]")
            print("daogang=" + daogang.text)
            if(daogang.text.find("不考虑")>=0):
                button_close = driver.find_element_by_xpath("//div[@id='recommendContent']/div[2]/div/div[2]/div/h3/div/span/i")
                button_close.click()
                print("到岗时间不符合要求:"+daogang.text)
            xinzi = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[2]/div/div/span[3]")
            print("xinzi=" + xinzi.text)
            #最高上限薪资
            if (xinzi.text!="面议" and int(xinzi.text.split("-")[1].replace("K",""))>18):
                button_close = driver.find_element_by_xpath("//div[@id='recommendContent']/div[2]/div/div[2]/div/h3/div/span/i")
                button_close.click()
                print("薪资超过上限:" + xinzi.text)
            #学历判断，学历可能存在两个位置
            if(isElementExist(driver,"//*[@id='resume-page']/div/div/div[2]/div[5]/div/div/div/h4")):
                xueli=driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[5]/div/div/div/h4")
                print("xueli="+xueli.text)
                if(xueli.text.find("大专")>=0 or xueli.text.find("专科")>=0 or xueli.text.find("非")>=0):
                    print("学历不符合要求:" + xueli.text)
                    button_close = driver.find_element_by_xpath("//div[@id='recommendContent']/div[2]/div/div[2]/div/h3/div/span/i")
                    button_close.click()
                    break
            elif isElementExist(driver, "//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div/h4"):
                xueli = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div/h4")
                print("xueli=" + xueli.text)
                if (xueli.text.find("大专")>=0 or xueli.text.find("专科")>=0 or xueli.text.find("非")>=0):
                    print("学历不符合要求:" + xueli.text)
                    button_close = driver.find_element_by_xpath("//div[@id='recommendContent']/div[2]/div/div[2]/div/h3/div/span/i")
                    button_close.click()
                    break
            #专业,专业也有两个位置
            if (isElementExist(driver, "//*[@id='resume-page']/div/div/div[2]/div[5]/div/div/div/h4/b[2]")):
                zhuanye = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[5]/div/div/div/h4/b[2]")
                print("zhuanye=" + zhuanye.text)
                #优先考虑计算机专业
                for zhuanye_tmp in zhuanye_arr:
                    if(zhuanye_tmp==zhuanye.text):
                        totolscore=40
            elif (isElementExist(driver, "//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div/h4/b[2]")):
                zhuanye = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div/h4/b[2]")
                print("zhuanye=" + zhuanye.text)
                # 优先考虑计算机专业
                for zhuanye_tmp in zhuanye_arr:
                    if (zhuanye_tmp == zhuanye.text):
                        totolscore = 40
            #技能
            jineng = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[1]/div[2]/div[2]")
            print("jineng=" + jineng.text)
            for jineng_tmp in jineng_arr:
                k=0
                if(jineng.text.find(jineng_tmp)>=0):
                   k=k+1
                if(k>=2):
                    totolscore = totolscore+20
                    break
            jingyan_list=driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[4]/div/div")
            print("项目经验："+str(jingyan_list.find_elements_by_tag_name('div').__len__()))
            for jinyan_tmp in jingyan_list.find_elements_by_tag_name('div'):
                if(j<int(jingyan_list.find_elements_by_tag_name('div').__len__())):
                    j=j+1
                    jinyan1=driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div["+str(j)+"]/div[1]/div")
                    print("jinyan1="+jinyan1.text)
                    for jinyan_tmp1 in jineng_arr:
                        k = 0
                        if (jineng.text.find(jinyan_tmp1) >= 0):
                            k = k + 1
                        if (k >= 2):
                            totolscore = totolscore+k*20
                    jinyan2 = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[2]/div[4]/div/div/div[" + str(j) + "]/div[2]/div")
                    print("jinyan2=" + jinyan2.text)
                    for jinyan_tmp2 in jineng_arr:
                        k = 0
                        if (jineng.text.find(jinyan_tmp2) >= 0):
                            k = k + 1
                        if (k >= 2):
                            totolscore = totolscore + k * 20
            #打招呼
            if(totolscore>=60):
                button_test4 = driver.find_element_by_xpath("//*[@id='resume-page']/div/div/div[3]/div/div[2]/div/div/div[2]/span/button")
                button_test4.send_keys()
                 # 关闭
                button_test4 = driver.find_element_by_xpath("//div[@id='recommendContent']/div[2]/div/div[2]/div/h3/div/span/i")
                button_test4.click()
                time.sleep(5)
finally:
    print("系统出错！")

import time
from selenium import webdriver
'''1、打开浏览器函数'''
def open_url(driver,url):
    driver.get(url)  # 打开浏览器对应的网址
    driver.maximize_window()

'''2、登录函数'''
def login_fun(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()


'''3、搜索'''
def sear_fun(driver,url,username,password,key):
    open_url(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")  ###方法一
    id_frame = id_li + "-frame"  # 得到frame id
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
    print(num)
    if "841" in num:
        print("搜索用例通过")
    else:
        print("搜索失败")
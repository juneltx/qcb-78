"""接口自动化、UI自动化（人工点、浪费时间，效率低下。枯燥）、APP自动化
UI自动化是人和浏览器界面的互动，代码代替人实现和浏览器之间的互动
代码---通过 浏览器驱动 将代码指令翻译给浏览器，使得浏览器做出响应
Chromedriver（如果用最新的可以，没有最新的可以用71版本，比较稳定，可以向前兼容高版本。低版本的驱动可以翻译高版本的浏览器
geckodriver
ieserverdriver
下载解压为chromedriver.exe,放至python安装目录文件夹下"""

##2、selenium工具，UI自动化工具，也是第三方库文件
'''selenium工具包括三个部分：
1、ide 用来录制脚本，用得少，不好用，录制脚本的工具难免会出错;
2、webdriver，库，提供了对网页操作的一些方法，结合python或java来使用；
3、grid 分布式，同时对多个浏览器实现并发测试
'''

#1\selenium安装好，2、驱动下载---python对应的安装目录；3、导入selenium webdriver
#导入selenium工具中的webdriver库
from selenium import webdriver
import time
driver=webdriver.Firefox()#初始化一个浏览器，初始化一个会话session
driver.get("http://baidu.com") #打开浏览器对应的网址
driver.maximize_window()
driver.get("https://taobao.com")
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
driver.close()
#关闭浏览器 close():关闭窗口，不会退出浏览器，,quit()退出当前会话，关闭浏览器，清楚缓存


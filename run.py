from common import method #导入公共方法
from test_data import test_data
from selenium import webdriver
driver=webdriver.Firefox()
driver.implicitly_wait(10)

url=test_data.data.get("url")
username=test_data.data.get("username")
password=test_data.data.get("password")
key=test_data.data.get("key")

num=method.sear_fun(driver,url,username,password,key)
if key in num:
    print("搜索用例通过")
else:
    print("搜索用例不通过")

'''简历里面写上：
熟悉python语言，能够结合selenium工具编写web自动化测试脚本、结合requests库简单编写接口自动化脚本
webUI自动化，利用python+selenium库实现web自动化，
利用python+requests库和openpyxl库实现接口自动化
1、你会自动化吗？不要直接说不会，要说参与过项目，但只有半年
2Python的数据类型，列表元组，字典，区别，90%会问到
3你的工作中哪些场景会用到字典？怎么用的?    答：利用对象属性，接口自动化测试数据存在字典中，字典方便读取数据。
4能否解释一下*args和**kwargs的区别？  答：一个是位置传参，一个是关键字传参，一个是存在元组里面，一个是存在字典里
都是不定长的，都需要前面的参数接收完再接收
5、python区分大小写
6、项目结构是什么样子的？哪些文件夹？分别用来存档哪些东西？自动化框架的组成
   自动化框架
7、python中标识符的命名规则?pep8规范，python之禅，python编写规范
8、python字符串的逆序输出怎么用？切片，负数
10、怎么取出两个列表中相同的元素，for嵌套
   for i in list1：#取相同元素
      for j in list2：
          if i==j：
          list3.append（i）
    for b in（list1+list2）
        if b not in list3：
        list4.append(b)
UI自动化问题
1、常用元素定位方法有哪些？最常用的是哪些？
2、xpath怎么写？多多练习
*3、浏览器里元素定位唯一，但是代码会报错，元素找不到，分析原因。答：①id动态变化 
②页面没有刷新出来，网比较慢，添加等待，③有些元素不可见 ④子页面，在子页面需要切换iframe
4、等待方式有哪些?强制、隐性
5、requests库怎么实现接口请求----百度---扩展
6、openpyxl怎么读取excel表格数据？
7、输出内容结果，有兴趣的了解

熟悉了解Robot Framework的自动化（特点，关键字驱动，，赠送RF工具的课程，不需要写代码也可以实现自动化，可以扩展，看录播，
在公司中也是一个主流的自动化框架，有精力看，多会一款工具有利于就业面的打开。


    
'''
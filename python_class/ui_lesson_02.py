"""web自动化通讯原理
1、chromedriver启动服务，IP端口监听
2、python webdriver 跟chromedriver建立连接，发送的http请求
3、chromedriver接收请求的指令之后，驱动浏览器把指令执行
4、chromedriver把结果返回给webdriver
接口自动化====接口最多，稳定，性价比最高的，提高回归测试的效率
UI自动化，测试数据少，性价比低，维护成本高，主要用于冒烟测试

web页面的基本组成：HTML+CSS+JS(Javascript)
html:定义页面呈现的内容：标签语言，<>值</>
css:控制页面如何呈现---布局设置，字体颜色、字体大小
JS：可以让页面在不同情形做不同事情

html页面：标签找属性
元素定位八大方法：id、name、xpath等
页面元素的定位：能够唯一标识这个元素的内容
按照开发遵循原则的基础上，通过元素属性里的id和name唯一标识
找到元素后的操作：
点击：click
发送：send keys

通过id name可以找到元素，大部分元素没有这两个属性时，用xpath！

*Xpath元素定位方法
1）html---body--div---div---div【1】----a-----small从根开始一级一级往下找，
有继承和顺序关系，是绝对路径，页面内容发生变化，表达方式就变了，不好维护
2）//*[@id="username"]相对路径，//+标签名+[@id=""]，其中id属性选择比较有标识性的

*层级定位
//标签名[@属性名=属性值]//标签名[@属性名=属性值]
-//div[@class="login-logo"]//b

*文本标识方法
//b[text()="柠檬ERP"]当值不变，可以通过本文来标识时，可以用这种方法，也挺常用

*包含属性值,值或属性内容太长，不好标识时可以用这种方法
//标签名[contains(text(),"柠檬")]
//标签名[contains(@name,"柠檬")]

*属性不唯一，轴定位，通过前或后标识属性唯一的元素来定位following sibling::
或者前面的兄弟preceding sibling::前面兄弟的标签名
例如//input[@id="rememberUserCode"]/following-sibling::ins通过后面的ins标签兄弟找到


##Python三大等待，一般打开新页面，在click操作之后，页面有刷新时间，需要等待
1、强制等待---sleep():设置等待时间没有到期，就算元素出现了，也还要等待，速度慢
2、智能等待--
   2.1隐性等待：默认等待时间，只要元素出现了，直接继续执行，一个会话只执行一次
       默认等待设置的市场，提前出现，提前执行，有些地方不生效，implicitly wait
   2.2显示等待----比较复杂，只要了解"""
#获取页面标题
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://erp.lemfix.com")
driver.maximize_window()
page_title=driver.title
if page_title=="柠檬ERP":
    print("这个页面的标题是{}".format(page_title))
else:
    print("这个页面的标题是{}".format(page_title))


#输入用户名和密码,点击登录按钮
import time
driver.find_element_by_id("username").send_keys("test123")
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()
time.sleep(2)
#点击零售出库
driver.find_element_by_xpath("//li[@class='treeview']//span").click()
time.sleep(2)
#driver.find_element_by_xpath("//span[text()="零售出库"]).click()

#报错，没有找到元素，原因，出现html页面里面嵌套有子html页面，识别路径，路径中包含的iframe，
# 直接定位不会成功，
# 需要切换页面，如何切换子页面
#driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys("712")
#driver.find_element_by_id("searchNumber").send_keys()

##如何切换子页面,iframe页面切换的第一种方法
#1、frame名字----找唯一标识 通过id name来定位，切换注意，如果id是变幻的，随机的，不可以直接作为元素来定位，没有任何规律的随机数#
#driver.switch_to.frame("tabpanel-8acbf12b8a-frame")#这种不行，因为中间是一串随机数，每次刷新都会变化，不唯一
id_li=driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")###方法一
id_frame=id_li+"-frame"#得到frame id
#driver.switch_to.frame(id_frame)

#方法2：通过web element元素定位的方式切换子页面，和第一种方法一样都需要掌握，还有一种标签法不要求掌握
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))

##接下来操作就是针对子页面的操作
driver.find_element_by_id("searchNumber").send_keys("841")
#点击查询
driver.find_element_by_id("searchBtn").click()
#前面的隐性等待结合强制等待，读取查询列表
time.sleep(1)

#获得单据编码的号码（文本）
num=driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)

if "841" in num:
    print("搜索用例通过")
else:
    print("搜索失败")


#确认登录用户名
page_name=driver.find_element_by_xpath("//p").text #获取这个元素的文本内容
if page_name=="测试用户":
    print("这个登录用户是{}".format(page_name))
else:
    print("这个用例不通过！")
#登录进去测试是否为测试用户
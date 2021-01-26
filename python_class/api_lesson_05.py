'''接口测试第三方库别人写好导入直接用cmd-pip install requests，缺乏权限加--user time out就切换源，源在群里
法二见文档
requests的方法传参除了url之外，其他必须要字典格式传参
'''
# import requests #没有小红曲线，灰色表示导入成功
#注册接口
# url_api="http://8.129.91.152:8766/futureloan/member/register"
# api_data={
#   "mobile_phone": "15811111111",
#   "pwd": "lemon1234",
#   "type":"1",
#   "reg_name":"python-1"
# }
# head={"X-Lemonban-Media-Type":"lemonban.v2"}
# response=requests.post(url=url_api,json=api_data,headers=head)#必须传的参数、默认、关键字参数
# print(response)#服务器响应200，有响应不一定是请求成功）
# print(response.json())#{'code': 1006, 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved', 'msg': '请求头X-Lemonban-Media-Type不存在'}
'''{'code': 0, 'msg': 'OK', 'data': {'id': 10199529, 'reg_name': 'python-1', 'mobile_phone': '15811111111'},
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}'''


#2登录接口
import requests,pprint
url_api2="http://8.129.91.152:8766/futureloan/member/login"
api_data2={
"mobile_phone": "15811111111",
"pwd": "lemon1234"
}
head2={"X-Lemonban-Media-Type":"lemonban.v2"}
response2=requests.post(url=url_api2,json=api_data2,headers=head2)#必须传的参数、默认、关键字参数
pprint.pprint(response2.json())
res=response2.json()
'''{'code': 0, 'msg': 'OK', 'data': {'id': 10199529, 'leave_amount': 0.0, 'mobile_phone': '15811111111', 
'reg_name': 'python-1', 'reg_time': '2021-01-19 12:45:56.0', 'type': 1, 
'token_info': {'token_type': 'Bearer', 'expires_in': '2021-01-19 12:55:00', 
'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk5NTI5LCJleHAiOjE2MTEwMzIxMDB9.dWWVgxVB9XIS2sjd03pVItY6YTCXYkKBV2GVOEYb-2GmKQ0YZVciUhEh99YgaB-kTsI_YXv971B0Vn1UOLF7aA'}}, 
'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}

{'code': 0, 'msg': 'OK', 'data': {'id': 10199529, 'leave_amount': 0.0, 'mobile_phone': '15811111111', 'reg_name': 'python-1', 'reg_time': '2021-01-19 12:45:56.0', 'type': 1, 'token_info': {'token_type': 'Bearer', 'expires_in': '2021-01-19 13:02:48', 'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk5NTI5LCJleHAiOjE2MTEwMzI1Njh9.pjGihInSY2I7ZCRw44TA-f4G1I3xwZFl-w5iPaFNAJ_vxZsvYCLgDci3Pr2uoS-CkG48YhuMlv7ZK2e-wsoz-g'}}, 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 10199529,
          'leave_amount': 0.0,
          'mobile_phone': '15811111111',
          'reg_name': 'python-1',
          'reg_time': '2021-01-19 12:45:56.0',
          'token_info': {'expires_in': '2021-01-19 13:02:48',
                         'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk5NTI5LCJleHAiOjE2MTEwMzI1Njh9.pjGihInSY2I7ZCRw44TA-f4G1I3xwZFl-w5iPaFNAJ_vxZsvYCLgDci3Pr2uoS-CkG48YhuMlv7ZK2e-wsoz-g',
                         'token_type': 'Bearer'},
          'type': 1},
 'msg': 'OK'}
'''

#充值接口

#法一
# member_id_recharge=res["data"]["id"]
# print(member_id_recharge)
# token_recharge=res["data"]["token_info"]["token"]#取key值
#法二
#充值法二：jsonpath，安装第三方库，导入结果放在列表里
# import jsonpath
# member_id_recharge=jsonpath.jsonpath(res,"$.data.id")[0]#jsonpath输出的是列表格式，取值的话默认【0】
# token_recharge=jsonpath.jsonpath(res,"$.data.token_info.token")[0]
#
# #法二的简写形式，偷懒写法可以不用数几个节点几层嵌套
# # member_id_recharge=jsonpath.jsonpath(res,"$..id")[0]#取id
# # token_recharge=jsonpath.jsonpath(res,"$..token")[0]#取token
# url_api3="http://8.129.91.152:8766/futureloan/member/recharge"
# api_data3={"amount":10000,"member_id":member_id_recharge}
# head3={"X-Lemonban-Media-Type":"lemonban.v2","Authorization":"Bearer"+" "+token_recharge}
# response3=requests.post(url=url_api3,json=api_data3,headers=head3)#必须传的参数、默认、关键字参数
# pprint.pprint(response3.json())
'''响应结果{'code': 0, 'msg': 'OK', 'data': {'id': 10199529, 'leave_amount': 0.0, 'mobile_phone': '15811111111', 
'reg_name': 'python-1', 'reg_time': '2021-01-19 12:45:56.0', 'type': 1, 
'token_info': {'token_type': 'Bearer', 'expires_in': '2021-01-19 12:55:00', 
'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjEwMTk5NTI5LCJleHAiOjE2MTEwMzIxMDB9.dWWVgxVB9XIS2sjd03pVItY6YTCXYkKBV2GVOEYb-2GmKQ0YZVciUhEh99YgaB-kTsI_YXv971B0Vn1UOLF7aA'}}, 
'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
充值的响应结果{'code': 0,
 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved',
 'data': {'id': 10199529,
          'leave_amount': 10000.0,
          'mobile_phone': '15811111111',
          'reg_name': 'python-1',
          'reg_time': '2021-01-19 12:45:56.0',
          'type': 1},
 'msg': 'OK'}
'''

##利用requests请求访问百度,若出现乱码，则需要手动指定解码方式，另一方面，会响应不正确的页面，避免
#爬虫导致瘫痪，反爬机制，服务器通过反扒机制比较是否为正常浏览器请求，
# 通过user-agent头部信息来请求，表示为正常请求
import requests,pprint
url_baidu="https://www.baidu.com/s"
param={"wd":"柠檬班"}#key是wd，值是柠檬班，url中加s，setting
head={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
response=requests.get(url=url_baidu,headers=head,params=param)
#print(response.text)#自动解码页面--不能解码成功---再用另外一种方法---优先--80%
print(response.content.decode("utf8"))#手动指定解码方式

#以上访问百度的请求和网页中查看源代码一致

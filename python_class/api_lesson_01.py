"""
标识符：
1、命名规则，只能包含数字、字母、下划线

import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']
"""
# print("我最喜欢的职业是软件测试！")
# # # print("快捷键注释ctrl加斜杠")
print(type("hey"))
#print(isinstance(12,bool)) 结果是True或False

'''字符串引号的用法三引号格式保持输出'''
print('''-------软件测试--------
时间：ABC
地点：XXX
''')

#变量
name="小君君"
#print(name)
print('''-----'''+name+'''基本信息----------
age：18  
gender：female
''')



#占位符，需求，在字符串中传入变量，又不想截断字符串，可以在字符串中占位，
# 在python中叫格式化输出，用format函数，要传变量的地方用,一个萝卜一个坑，占位符可以为空，按照默认顺序传参，否则，可以写上位置索引
name="小君君君"
gender="女孩子"
age=18
amount=10000.08
print('''{}个人资料----------
姓名：{}
性别：{}
年龄：{}
存款：{}'''.format(name,name,gender,age,amount))

#占位符指定顺序
name="小君君君"
gender="女孩子"
age=18
amount=10000.08
print('''{2}个人资料----------
姓名：{1}
性别：{1}
年龄：{3}
存款：{4}'''.format(name,name,gender,age,amount))
# 女孩子个人资料----------
# # 姓名：小君君君
# # 性别：小君君君
# # 年龄：18
# # 存款：10000.08
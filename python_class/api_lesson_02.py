# 在python中叫格式化输出，用%来，要传变量的地方用,一个萝卜一个坑，占位符可以为空，按照默认顺序传参，否则，可以写上位置索引
# name="小君君君"
# gender="女孩子"
# age=18
# amount=10000.08
# print('''%s个人资料----------
# 姓名：%s
# 性别：%s
# 年龄：%d
# 存款：%f'''%(name,name,gender,age,amount))

# 小君君君个人资料----------
# # # 姓名：小君君君
# # # 性别：女孩子
# # # 年龄：18
# # # 存款：10000.080000

#字符串的操作----索引取值[0]第一个值，【-1】最后一个值；
# 取多个值:切片【索引头：索引尾+1：步长】规则是取头不取尾，如果说想取到尾部，则索引尾多算一个步长
#索引头默认值为0，索引尾默认到最后，步长默认1
# str='hellowang  lukai'
# print(str[9])
# print(str[-1])
# print(str[::])
# print(str[0:9])
# print(len(str))
#
# #获取某个元素的索引 .index('i')获取字符串中i元素的索引
# # .find('i')也可以用于获取索引,找到第一个出现的索引并返回
# # 区别：index没有找到元素的话会报错，代码无法继续运行，find会继续运行，返回-1说明没有找到
# print(str.index('l'))
# print(str.find('l'))
#
# #.count('1')统计1出现的次数；.replace（'old','new')
# print(str.replace('lukai','junjun'))

#+的用法，加法、拼接字符串;-不支持-------*除了支持两个数相乘的结果，还支持字符串的重复输出,除法结果为float
#数据类型强制转换 str() int() float()

# print(10+20)
# print('123'+'456')
# print('100'+'ning')
# print(str(100)+'ning')
# print('love you'*100)
#input 函数 从控制台获取输入内容，默认全部是字符串格式
# content=int(input('请输入任意数字：'))
# print(type(content))
# print(content)


#赋值运算符---符号右边的内容赋值给左边=，+=，-= a=10,a+=10
#比较运算符 >,<,==,<=,>=,!=，运算结果是布尔值 print(4>5 ) False
#逻辑运算符：and   or not  print(not 5<9) False
#成员运算符，in not in
# str1="i love u baby"
# print("i" in str1)
#结果True

#作业第一题
# name1=str(input("请输入姓名："))
# age1=int(input("请输入年龄："))
# gender1=str(input("请输入性别："))
# print('''***************
# 姓名：{}
# 性别:{}
# 年龄：{}
# ********************'''.format(name1,gender1,age1))


'''作业第二题
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
3）替换python为 “lemon”.
4) 找到aaa的起始位置'''
#（1）
print('（1）')
str1='python hello aaa 123123aabb'
print(str1[0:6])
#（2）
print('（2）')
print("'o a'是str1的成员吗？答案是：")
print('o a'in str1)
print("'he'是str1的成员吗？答案是：")
print('he'in str1)
print("'ab'是str1的成员吗？答案是：")
str2='ab'
print(str2 in str1)
#(3)
print('(3)')
print(str1.replace('python','lemon'))
#(4)
print('(4)')
print(str1.index('aaa'))

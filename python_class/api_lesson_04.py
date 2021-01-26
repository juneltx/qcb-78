#非默认前于默认参数，不定长参数利用位置传参方式接收多余参数,不一定在传参数时放最后,
# **kwargs，利用关键字方式传参，用字典保存多余参数，传参时一定要放在最后
'''
def good_job(salary,bonus,subsidy=500,*args,**kwargs):
    print("salary为{}".format(salary))
    print('bonus为{}'.format(bonus))
    print('subsidy为{}'.format(subsidy))
    print('*args为{}'.format(args))
    print('**kwargs为{}'.format(kwargs))
    sum1=salary+bonus+subsidy
    for num in args:
      sum1+=num
    for j in kwargs:
        sum1+=kwargs[j]
    print('工资总额为{}'.format(sum1))

good_job(8000,2000,800,100,200,300,aa=100,bb=200)#调用函数---传参--实参
'''

'''
拿到薪资总和，做一个判断，是不是一个好的工作？
返回值：函数如果有一个数据需要给到调用这个函数的人进行使用，则吧这个数据的变量设为返回值
'''
# def good_job(salary,bonus,subsidy=500,*args,**kwargs):
#     print("salary为{}".format(salary))
#     print('bonus为{}'.format(bonus))
#     print('subsidy为{}'.format(subsidy))
#     print('*args为{}'.format(args))
#     print('**kwargs为{}'.format(kwargs))
#     sum1=salary+bonus+subsidy
#     for num in args:
#       sum1+=num
#     for j in kwargs:
#         sum1+=kwargs[j]
#     return sum1,salary#定义函数的返回值,返回值一定在函数最后，返回值后面的代码不会被执行；
#     # 返回值可以没有None，可以有多个，返回值之间用逗号隔开，元组接收，return sum1，salary
#     print('工资总额为{}'.format(sum1))
#
# result=good_job(8000,2000,800,100,200,300,aa=100,bb=200)#result变量接收函数的返回值
# print('工资总和为{}'.format(result))
# if result[0]>=10000:
#     print("it's a good job")
# else:
#     print("its not a good job")

'''内置函数：print(),input(),type(),isinstance(),len() ;
数据类型：str(),int(),float(),list(),tuple(),dict(),set(),bool(）
字符串内置方法.format，index，replace，find
列表内置方法:append,insert,pop,remove,extend,count
字典内置：pop,update,get
range()'''

'''作业
1、把字符串转为列表 list()'''
# str1="hello python lesson"
# list1=list(str1)
# print(list1)
# #结果：['h', 'e', 'l', 'l', 'o', ' ', 'p', 'y', 't', 'h', 'o', 'n', ' ', 'l', 'e', 's', 's', 'o', 'n']
# # #扩展["hello","python","lesson"] split(str,num)，将字符串以预定内容截断,num是截取次数
#
# list2=str1.split(" ",1)#['hello', 'python lesson']
# list3=str1.split(" ",2)#['hello', 'python', 'lesson']
# print(list3)
# #
# 2. 完成任意整数序列的相加 - 生成一个整数序列，里面全是数字。求里面所有数字的和
num1=int(input("please input a num"))
sum1=0
for i in range(num1):
    sum1+=i
print(sum1)

def add_int(num3):
    sum2=0
    for j in range(num3):
        sum2+=j
    return sum2

result=add_int(100)
print(result)
#结果please input a num100 4950 4950
# 3、定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，
# 如果大于5，输出True；否则输出False。--if 判断嵌套'''
def object(subject):
    if type(subject)==list or type(subject)==dict or type(subject)==str:
        length=len(subject)
        if length>=5:
            print("True")
        else:
            print("False")
    else:
        print("数据类型不能计算长度！")

object([1,2,3,4])

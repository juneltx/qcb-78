
#list 列表，可以存放任意数据类型，包括列表，len（），取值每个元素的位置为索引
"""list1=[20,3.14,'wanglukai',[1,2,3,4],True]
print(len(list1))
print(list1[3][0])#列表嵌套取值
print(list1[-1])

#列表元素可以修改，增删改
list1.append('jobhunting')#追加元素至末尾
list1.insert(1,"插入至1号索引")#指定索引
print(list1)
list1.extend(["扩展合并1","扩展合并2","扩展合并3"])
print(list1)
list1.pop()#默认删除最后一个元素,但可以指定
print(list1)
list1.pop(1)
print(list1)

list1.remove("扩展合并2")#指定内容删除
print(list1)
#list1.clear()#清空列表，一般不用

#修改重新赋值
list1[0]="重新赋值的0号"
print(list1)

#列表元素可以重复，并通过count来统计个数
print(list1.count("重新赋值的0号"))

#元组 tuple，特性和list相似，元组的元素不可以改变！
tuple1=('1',3,[1,2,3],False)
list2=list(tuple1)
print(list2)
list2[0]='强制转换成list才可以对元组元素改变'
print(list2)
tuple2=tuple(list2)
print(tuple)#万不得已才来回转换，作为拓展了解

##字典 dict{}
'''1 元素是键值对的格式： key：value，一个键值对是一个元素，多个元素逗号隔开
 2、字典一般使用场景：描述一个物件的属性
3 字典在3.6版本之前无顺序，取值，通过key来取value值
4.key不可以变，不可以是列表和字典，key不可以重复，唯一性，value的要求没有任何要求，可以改变增删改查'''
dict1={"name":"junjun","age":18,"gender":"female"}
print(dict1["age"])
print(dict1.get("age"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#增加一个键值对
dict1["hobby"]="带娃"#如果key不存在，则增加一个键值对，、
# 如果key存在，则更新一个键值对的value
dict1["gender"]="male"
print(dict1)

#删除----指定key进行元素删除，因为没有顺序
print(dict1.pop("hobby"))
print(len(dict1))
#字典的多个元素追加
dict1.update({"city":"wx","weight":"130"})
print(dict1)

'''集合：set{}，元素单个，集合的元素不重复，会自动去重
'''
#获取列表中出现过的元素---去重
list3=[1,2,3,3,44]
set1=set(list3)
print(set1)
list4=list(set1)
print(list4)

'''控制流：if判断和for循环
if 条件:(条件为1 永远True）
   子代码
elif 条件：
    子代码
else：
   子代码'''
# money=int(input("输入你有多少钱："))
# if money>=10000:
#     print("投资")
# elif money>5000:
#     print("打工")
# else:
#     print("乞讨")

'''for循环'''
# str3="软件测试工程师12345"
# count=0
# for i in str3:
#     print(i)
#     print('*'*20)
#     count+=1
# print(count)

list5=['1',[1,2,3],40]
for element in list5:
    if element==40:
        break#跳出整个循环，中断
       # continue #跳出一次循环
    print(element)

'''for循环一起结合使用的内置函数 range（）
start：默认从0开始
stop 到谁结束
step'''
for num in range(0,11,2):#取出0-10的偶数
    print(num)

dict5=dict(name="ning",city="wuxi")

'''作业
1：a=[1,2,'6','summer'] 
请用成员运算符判断 i是否在这个列表里面'''

a=[1,2,'6','summer']
if 'i' in a:
    print("'i'在列表a中")
else:
    print("'i'不在列表a中")

#输出结果为：‘i’不在列表a中

'''2：dict_1={"class_id":45,'num':20} 
请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。'''
dict_1={"class_id":45,'num':20}
num=dict_1.get('num')
if num>5:
    print('上课人数为{}'.format(num))
else:
    print('人数小于5')
"""
'''3.list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
列表当中的每一个值包含：姓名、性别、年龄、城市。以字典的形式表达。并且把字典都存在新的 list中，最后打印最终的列表。
方法1： 手动扩充--字典--存放在列表里面；{} --简单
方法2： 自动--dict（）--不强制-- for循环 ，list.append() --- 难度'''
'''list1 = ['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list1[0]={"姓名":"肥兔","性别":"男","年龄":18,"城市":"北京"}
list1[1]={"姓名":"鹿鹿","性别":"女","年龄":17,"城市":"上海"}
list1[2]={"姓名":"Freestyle","性别":"男","年龄":16,"城市":"天津"}
list1[3]={"姓名":"等","性别":"男","年龄":15,"城市":"上海"}
list1[4]={"姓名":"地球","性别":"男","年龄":18,"城市":"深圳"}
list1[5]={"姓名":"阑珊","性别":"女","年龄":17,"城市":"北京"}
list1[6]={"姓名":"柠檬","性别":"女","年龄":18,"城市":"广州"}
print(list1)

dict1={"name":"1","gender":"male","age":18,"city":"sz"}
dict2={}
dict3={}
dict4={}
dict5={}
dict6={}
dict7={}
list1=[dict1,dict2,dict3,dict4,dict5,dict6,dict7]
print(list1)
'''
# list1=['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
# list2=[]
# for i in list1:
#     dict1=dict(name=i,gender="female",age=18,city="北京")
#     list2.append(dict1)
# print(list2)

list1=['肥兔', '鹿鹿', 'Freestyle', '等', '地球', '阑珊', '柠檬']
list3=['male','female','male','female','male','female','male']
list4=[18,19,20,21,22,23,24]
list5=['北京','北京','北京','北京','北京','北京','北京']
list2=[]
for i in range(len(list1)) :
    dict1=dict(name=list1[i],gender=list3[i],age=list4[i],city=list5[i])
    list2.append(dict1)
print(list2)

'''4、for循环遍历其他的数据类型 --字典'''
# dict1={"name":"junjun","age":18,"gender":"female","hobby":"film"}
# for element in dict1:
#     print('''{}:{}'''.format(element,dict1[element]))
    # print(dict1.get("age"))
    # print(dict1.keys())
    # print(dict1.values())
    # print(dict1.items())



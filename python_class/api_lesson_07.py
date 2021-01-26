'''接口自动化测试的基本流程：
1、根据接口文档拟写接口测试用例，然后写在excel里
2、执行测试--利用requests库的requests函数执行，将执行结果获取
3、执行结果和预期结果进行对比，判断是否通过，得到最终结果
4、最终结果写入excel表格，pass或failed'''


##读取函数的方法，python package中导入；注意：excel表格读取的数字文本，是字符串
# eval():从字符串中获取python表达式，脱掉引号，获取字典
from python_class import api_lesson_06
def execute_fun(filename,sheetname):
    cases=api_lesson_06.read_data("test_case_api.xlsx","register")#调用读取数据的函数,返回存有字典的列表
    for case in cases:
        case_id=case.get("case_id")
        url=case.get("url")#通过key 取url地址
        data=eval(case["data"]) #取测试参数,脱去引号转换为字典
        expected_result=case.get("expected_result")
        expected_result=eval(expected_result)
        expected_msg=expected_result.get("msg")
        # print(url,data,expected_result)#确认下取得对不对
        real_result=api_lesson_06.api_func(url_api=url,data_api=data)#调用接口发送参数
        real_msg=real_result.get("msg")
        print(real_result)
        print(expected_result)#问开发唯一标识执行结果的字段来比较
        print("真实执行结果：{}".format(real_msg))
        print("预期执行结果：{}".format(expected_msg))
        if real_msg==expected_msg:
            final_result="passed"
            print("第{}条测试用例通过".format(case_id))
        else:
            final_result="failed"
            print("第{}条测试用例不通过".format(case_id))
        print("*"*20)
        api_lesson_06.write_result("test_case_api.xlsx","register",final_result,case_id+1,8)
execute_fun("test_case_api.xlsx","register")


'''自动化框架包括：common基础代码脚本文件，模块、conf配置文件、test-data测试数据，
test-result测试结果（html报告+日志）、run.py启动文件，具体自动化框架是在自动化班进行讲解'''
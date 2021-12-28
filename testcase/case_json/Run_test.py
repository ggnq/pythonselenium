#Run_Test.py# -*- coding: utf-8 -*-

import sys
sys.path.append("G:/uni_test")
#添加当前过程的目录
import json
from run_method import RunMethod
from get_data import GetData
from depend_data import DependentData
from send_email import SendEmail

class RunTest:
    def __init__(self):
        self.runmethod = RunMethod()
        self.data = GetData()

    #程序执行
    def go_on_run(self):
        res = None
        #如果有10行，循环遍历每一行,从0行开始
        rows_count = self.data.get_case_lines()
        #排除0行，从第1行开始
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)#传入行数
                # request_data = self.data.get_data(i)
                header = self.data.is_header(i)
                #print(i)
                depend_case = self.data.is_depend(i)
                # return res
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data  # 更新值
                res = self.runmethod.run_main(method, url, data, header)
                # return res
                self.data.write_result(i, res)
                print(i)
                print(res)

                if self.com_util.is_contain(expect, res):
                    self.data.write_result(i, 'pass')
                    pass_count.append(i)
                else:
                    self.data.write_result(i, res)
                    fail_count.append(i)
                print(pass_count)
                print(fail_count)
            self.send_mail.send_main(pass_count, fail_count)

            else:
                print('失败')
            # if is_run :
            #     res = self.runmethod.run_main(method,url,data,header)
            #     return res
            # else:
            #     return None


if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
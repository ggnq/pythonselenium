#depend_data.py


from testcase.case_excel import OperationExcel
from run_method import RunMethod
from get_data import GetData
from jsonpath_rw import jsonpath, parse


class DependentData(object):
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()
        self.runmethod = RunMethod()

    """根据caseid获取该case的整行数据"""
    def get_case_line_data(self, case_id):
        rows_data = self.opera_excel.get_rows_data(case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        run_num = self.opera_excel.get_row_num(self.case_id)#拿到caseid的行号
        request_data = self.data.get_data_for_json(run_num)#拿到请求数据
        header = self.data.is_header(run_num)
        method = self.data.get_request_method(run_num)
        url = self.data.get_request_url(run_num)
        res = run_method.run_main(method, url, request_data, header)
        return json.loads(res)

    #拿到执行结果后，根据依赖数据规则提取这个数据
    def get_data_for_key(self, row):
        depend_data = self.data.get_depend_key(row)#拿到依赖数据
        response_data = self.run_dependent()#拿到返回数据
        json_exe = parse(depend_data)#按照dependdata的规则在结果集里面查找
        madle = json_exe.find(response_data)
        return [math.value for math in madle][0]
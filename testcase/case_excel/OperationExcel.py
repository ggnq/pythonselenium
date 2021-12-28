
import xlrd


class OperationExcel:
    """    docstring for ClassName 构造函数__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数
    """
    def __init__(self, file_name=None, sheets_id=None):  #把文件名和id默认为none，可以不传
        if file_name:                                   #如果传了文件名就使用它
            self.file_name = file_name
            self.sheets_id = sheets_id
        else:
            self.file_name = 'D:/Excel.xls'             #没有传文件名就用这个默认的文件和id
            self.sheets_id = 0
        self.data = self.get_data()                     #把获取到的表单内容赋给data

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheets_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取单元格的列数
    def get_cells(self):
        tables = self.data
        return tables.ncols

    # 获取单元格的内容
    def get_cell_value(self, row, col):
        tables = self.data.cell_value(row, col)
        return tables

    # 写入数据
    def write_value(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)  # 打开文件
        write_data = copy(read_data)  # 复制文件
        sheet_data = write_data.get_sheet(0)  # 获取第一个表
        sheet_data.write(row, col, value)  # 写入数据
        write_data.save(self.file_name)

    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)#根据caseid拿到行号
        rows_data = self.get_row_values(row_num)#根据行号拿到行的数据
        return rows_data

    #根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0    #行号初始为0
        clols_data = self.get_cols_data()
        for col_data in clols_data:
            if case_id in col_data:
                return num  #如果依赖id和caseid相等，返回行号
            num = num+1

    #根据行号找到该行的内容
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id != None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    operas = OperationExcel()  #实例化
    print(operas.get_cell_value(1,2))  #调用方法,获取第2行第2列
    print(operas.get_lines())  #调用方法,获取行数
    print(operas.get_cells())  #调用方法,获取列数
    print(operas.get_data())  #调用方法,获取表单
import xlrd
wb = xlrd.open_workbook('test.xlsx') #打开一个workbook

wb.sheet_names() #获取所有的sheet name


wb.nsheets #获取sheet 数量


wb.sheets() #获取所有sheet 对象


wb.sheet_by_name('Sheet1') #通过sheet名字查找


wb.sheet_by_index(0) #通过index查找


ws = wb.sheet_by_name('Sheet1')
ws.nrows #总行数
ws.ncols #总列数


ws.row_values(0,3,4) #获取第1行，第3~4列的值（不包含4）
ws.col_values(0,1,3) #获取第1列，第1~3行的值（不包含3）

ws.row(0)[0].value #获取第0行，第1列的值
ws.col(0)[0].value #获取第1列，第0行的值

ws.cell(0,2).value #获取特定单元格的值
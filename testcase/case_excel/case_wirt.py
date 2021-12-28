import xlwt
wb = xlwt.Workbook(encoding='utf-8') #新建一个workbook
wb.save('test.xlsx') #保存


ws = wb.add_sheet('Sheet2') #新建一个sheet2
ws.write(0,0,'value') #向第1行，第1列写入值

style = xlwt.XFStyle() #新建一个style
font = xlwt.Font() #新建一个font
font.name = 'Times New Roman' #设定字体
font.bold = true #黑体
font.underline = ture #下划线
font.italic = ture #斜体
style.font = font #设定style

ws.write(0,0,'value',sytle) #带样式写入值


#日期
style = xlwt.XFStyle()

style.num_format_str = 'M/D/YY'
# 其它的格式还有: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0

ws.write(0, 0, datetime.datetime.now(), style)

#公式
ws.write(1, 1, xlwt.Formula('SUM(A1,B1)'))

#超连接
ws.write(0,0,xlwt.Formula('HYPERLINK(http://www.baidu.com)'))


合并单元格
ws.write_merge(0,1,0,3,'value') #合并第1行，第2行的第1列，第4列，并写入值‘value’

对齐
alignment = xlwt.Alignment() # 新建一个 Alignment alignment.horz = xlwt.Alignment.HORZ_CENTER
# 其它的格式还有 HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED

alignment.vert = xlwt.Alignment.VERT_CENTER
#其它的格式还有 May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

style = xlwt.XFStyle()
style.alignment = alignment
ws.write(0, 0, 'value', style)


边框
borders = xlwt.Borders()
borders.left = xlwt.Borders.DASHED
#DASHED：虚线；NO_LINE：没有；THIN实线
style = xlwt.XFStyle()
style.borders = borders
worksheet.write(0, 0, 'value', style)

背景颜色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 0 #前景色
pattern.pattern_back_colour = 1 #背景色
style = xlwt.XFStyle()
style.pattern = pattern
ws.write(0, 0, 'value', style)
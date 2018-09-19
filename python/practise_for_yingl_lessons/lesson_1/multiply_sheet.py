from openpyxl import Workbook

#在内存中创建一个workbook对象
wb = Workbook()

ws = wb.get_active_sheet()
print(ws.title)
ws.title = '99乘法表'

#设置单元格的值
for row in range(1,10):
    for col in range(1,10):
        ws.cell(row = row, column = col).value = row * col

#最后保存
wb.save(filename='99乘法表.xls') 

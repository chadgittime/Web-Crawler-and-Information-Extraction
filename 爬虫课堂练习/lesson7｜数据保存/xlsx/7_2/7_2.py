# 导入模块openpyxl
import openpyxl

# 创建新的workbook对象
wb = openpyxl.Workbook()
# 获取工作簿的活动表
sheet = wb.active
# 给工作表重命名为new title
sheet.title = 'new title'
# 给A1单元格赋值
sheet['A1'] = 'hello'
# 要写入的多行内容写成列表，再放进大列表，赋值给rows
rows = [['hello', 'world'], ['你好', '世界']]
# 写入多行内容
for row in rows:
    sheet.append(row)
# 打印rows
print(rows)
# 保存新建的excel文件
wb.save('hello.xlsx')

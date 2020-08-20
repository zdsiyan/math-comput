import random
from random import choice
import xlsxwriter
import numpy as np



def writeCalc(filename):
    workbook = xlsxwriter.Workbook(f'{filename}.xlsx')
    ws1 = workbook.add_worksheet('算式')
    ws2 = workbook.add_worksheet('答案')
    # 样式
    ws1.set_column('A:A', 6)
    ws1.set_column('B:B', 18)
    ws1.set_column('C:C', 18)
    ws1.set_column('D:D', 18)
    ws1.set_column('E:E', 18)
    ws1.set_default_row(28)
    format = workbook.add_format()
    format.set_font_size(12)
    # 表头
    headings = ['计时', '____________分', '____________分', '____________分', '____________分']
    ws1.write_row('A1', headings, format)

    # 算式
    ops = ('＋','－','×','÷')
    ans = []
    i = 0
    cols = []
    while i < 100 :
        op1 = choice(ops)
        op2 = choice(ops)
        n = random.randint(1,9)
        if op1 == '＋' and op2 == '＋' :
            a = random.randint(0,100)
            b = random.randint(0,100-a)
            c = random.randint(0,100-a-b)
            ans.append(a + b + c)
        elif op1 == '＋' and op2 == '－' :
            a = random.randint(0,100)
            b = random.randint(0,100-a)
            c = random.randint(0,a+b)
            ans.append(a + b - c)
        elif op1 == '＋' and op2 == '×' :
            b = random.randint(0,9)
            c = random.randint(0,9)
            a = random.randint(0, 100 - b * c)
            ans.append(a + b * c)
        elif op1 == '＋' and op2 == '÷':
            c = random.randint(1, 9)
            b = n * c
            a = random.randint(0, 100 - b / c)
            ans.append(a + b / c)
        elif op1 == '－' and op2 == '＋' :
            a = random.randint(0,100)
            b = random.randint(0,a)
            c = random.randint(0,100-a+b)
            ans.append(a - b + c)
        elif op1 == '－' and op2 == '－' :
            a = random.randint(0,100)
            b = random.randint(0,a)
            c = random.randint(0,a-b)
            ans.append(a - b - c)
        elif op1 == '－' and op2 == '×' :
            b = random.randint(0,9)
            c = random.randint(0,9)
            a = random.randint(b*c,100)
            ans.append(a - b * c)
        elif op1 == '－' and op2 == '÷':
            c = random.randint(1, 9)
            b = n * c
            a = random.randint(100 - b / c,100)
            ans.append(a - b / c)
        elif op1 == '×' and op2 == '＋' :
            a = random.randint(0, 9)
            b = random.randint(0, 9)
            c = random.randint(0,100-a*b)
            ans.append(a * b + c)
        elif op1 == '×' and op2 == '－' :
            a = random.randint(0,9)
            b = random.randint(0,9)
            c = random.randint(0,a*b)
            ans.append(a * b - c)
        elif op1 == '÷' and op2 == '＋' :
            b = random.randint(1, 9)
            a = n * b
            c = random.randint(0,100 - a / b)
            ans.append(a / b + c)
        elif op1 == '÷' and op2 == '－' :
            b = random.randint(1,9)
            a = n * b
            c = random.randint(0,a / b)
            ans.append(a / b - c)
        else :
            continue

        cols.append(f"{a}{op1}{b}{op2}{c}=")
        i += 1

    cells = np.split(np.array(cols), 4)
    ws1.write_column('B2', cells[0], format)
    ws1.write_column('C2', cells[1], format)
    ws1.write_column('D2', cells[2], format)
    ws1.write_column('E2', cells[3], format)

    cells = np.split(np.array(ans), 4)
    ws2.write_column('B2', cells[0], format)
    ws2.write_column('C2', cells[1], format)
    ws2.write_column('D2', cells[2], format)
    ws2.write_column('E2', cells[3], format)

    workbook.close()
#print("*" * 60)
#i = 0
#while i < len(ans):
#    print("第%s题的答案是：%d" % (i + 1, ans[i]))
#    i += 1
# TODO 转换成exe程序，输入文件名，默认当天日期
# https://www.cnblogs.com/mini-monkey/p/11195309.html

writeCalc("混合运算")

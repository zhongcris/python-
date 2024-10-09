# 实战4：嵌套循环：输出一个菱形，要求行数：奇数
'''
line=eval(input('输入行数: '))
top_line=(line+1)//2
bottom_line=line-top_line
if line%2==0:
    print("重新输入:")
    line=eval(input(''))
for i in range(1,top_line+1):  # 此处可以不从1开始，如果不从1开始，则第一行不打印*，因为range(0)不执行
# 上三角
    for j in range(top_line-i):
        print(' ',end='')
    for k in range(2*i-1):
        print('*',end='')
    print()
# 下三角
for i in range(1,bottom_line+1):
    for j in range(i):
        print(' ',end='')
    for k in range(2*bottom_line-2*i+1): # 倒三角的难点在于总结出这个公式
        print("*",end='')
    print()
'''

# 实战5： 打印空心菱形 ，在打印空心的时候，计数必须和数学公式一样，从1开始循环，否则判断会出问题
line = eval(input('输入行数: '))
top_line = (line+1)//2
bottom_line = line-top_line
if line % 2 == 0:
    print("重新输入:")
    line=eval(input(''))
for i in range(1,top_line+1):
#  上三角
    for j in range(top_line-i):
        print(' ' , end='')
    for k in range(1, 2*i):  # 此处必须从1开始计数，因为数学表达式是从1开始总结的公式，尤其是在求空心菱形时
        if k == 1 or k == 2*i-1:
            print("*", end='')
        else:
            print(' ', end='')
    print()
# 下三角
for i in range(1,bottom_line+1):
    for j in range(i):
        print(' ', end='')
    for k in range(2*bottom_line-2*i+1): # 倒三角的难点在于总结出这个公式
        print("*", end='')
    print()

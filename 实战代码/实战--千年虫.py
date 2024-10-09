# 需求： 已知一个列表中存储的是员工的出生年份[88,89,90,98,00,99],由于时间比较久，出生的年份均为2位数，现在2位年份前加19，如果是00，则加200
list=[88,89,90,98,00,99]
print('原列表是:',list)

# 遍历列表方式
# for i in range(len(list)):
#if list[i]!=00:
#       list[i]='19'+str(list[i])  # 因为这里需要拼接，所以必须str转换成字符串类型的
#   else:
#      list[i]='200'+str(list[i])
print(list)

# 第二种方式：使用enumerate函数
for index,value in enumerate(list):
    if value!=00:
        list[index]='19'+str(value)
    else:
        list[index]='200'+str(value)
print(list)

'''
需求：假设北京到上海有四个车次可选，用户选择所要购买的车次，进行购票进站
'''
# 对应车次信息可以使用字典结构进行存储
dct_ticket={
    'G1234':['北京南-上海虹桥','09:00',' 14:00'],
    'G2345':['西安北-上海虹桥','10:00',' 18:00'],
    'G3456':['南京南-上海虹桥','11:00',' 13：30'],
    'G4567':['杭州东-上海虹桥','12:00',' 13：00']
}
print('车次 ',' 始发地', ' 目的地', '始发时间', '到达时间')
# 这里先遍历key，然后根据key遍历value，因为这样可以把列表的[]去掉
for key in dct_ticket.keys():
    print(key,end=' ')
# 这是根据key值遍历value，如果没有对应的value，则会返回none.上一个实战使用的是dct_ticket[key]的方法,如果没有对应的，则会报错
    for item in dct_ticket.get(key):
        print(item,end=' ')
    print()
usr_ticket=input('要购买的车次是：')
# 这个循环不对,这是C语言思路。原因是，这里的usr_ticket被python理解为一个新的变量，并不是我们输入的，所以遍历不到
# for usr_ticket in dct_ticket.keys():
#    if usr_ticket==dct_ticket.keys:
#         for item in dct_ticket.get(usr_ticket):
#              print('已购买的车次为：',usr_ticket,'车次信息是：',item,'乘车人为：')
info=dct_ticket.get(usr_ticket)
# 如果车次不存在
if info!=None:
    # 这里使用input.split函数，如果只用input，则解释器会把输入整体看作一个字符串,而这个函数会根据分隔符，看作多个输入
    user = input('乘车人信息是,多人请用逗号分隔:').split(' ')
    print('已购买的车次为：', usr_ticket, '车次信息是：', info[0], '发车时间为', info[1],'到达时间为',info[2], '乘车人为：', user)
else:
    print('改车次不存在!')
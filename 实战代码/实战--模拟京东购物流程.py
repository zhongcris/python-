'''
从键盘录入五个商品信息，添加到商品列表中，展示商品信息，提示用户选择商品，用户选中的商品添加到购物车中（购物车商品逆序）
用户选中的商品不存在需要有相应提示，当用户输入Q时，结束循环，显示购物车中的商品
'''
# 首先新建空字典存放商品信息，使用字典的原因是，商品信息和编号分离，更贴合实际一些
dct1={}
while True:
    key=eval(input('输入商品编号：'))
    if key!=0 :  #设定商品编号为0时，退出输入
        value=input('请输入商品：')
        dct1[key]=value
    else:
      break
print(dct1.values())
lst1=[]
lst=[]
while True:
    ord=input('输入指令:1.ls（查看商品） 2.add（添加购物车） 3.q（退出操作）：')
    if ord=='q':
        break
    elif ord=='ls':
        print(dct1)
    elif ord=='add':
        while True:
           num=eval(input('输入商品编号：'))
           if num!=0:
              for key in dct1.keys(): #这里的key实际上是一个新变量，和字典没有任何关系
                if key==num:
                  lst1=list(dct1[key])# dct1[key]和dct1.get(key)是取key值对应的value值，当然也可以根据value取对应的key,但是比较复杂一些
                  lst.append(lst1)
                  lst.reverse()
                  print('购物车商品为：', lst)
           else:
               break
    else:
      print('错误指令，重新输入：')



# python学习笔记
- 程序设计语言，又叫编程语言，可分为：机器语言、汇编语言、高级语言
  - 计算机程序就是使用编程语言组织起来的一组计算机指令
  - 采用编译方式执行的语言称为静态语言（Java）
  - 采用解释方式执行的叫做脚本语言（python）
  - python中一切皆对象

## 第一章
### 1.什么是类？     
类:是讲同一类对象的共同属性和行为抽象出来形成的一个复杂数据结构,与结构体类似，都是为了描述一个复杂的对象    
而对象是：现实世界的对象在程序中的模拟
- 类---->是同一类对象的抽象
- 对象--->是类的某一特定实体

类是结构体的延伸    
    
### 2.print函数   
在使用时，还可使用+号连接两个字符串或是两个同类型的变量，如果是不同类型的，那么使用逗号分隔开即可    
内置函数open为新建文件，新建文件并写完具体操作之后，需要close关闭文件
 ```python
print("x")  
print(chr(100),'who are U',sep='_',end='\t')    
print('value',...,sep='',end='\n',file=None)  
 ```
### 3.input函数  
默认输入的是字符串类型，若需要其他类型，可以在输入的时候直接进行类型转换
```python
a=int(input())
print(a+10)
```
### 4.代码缩进：
- 例如 “类”的定义；“函数”的定义等  
- 保留字，使用keyword可以查询 
```python
import keyword
print(keyword.kwlist) 
```

### 5.标识符命名规则:
1.可以是中文、英文、下划线和数字，第一个字符不能是数字    
2.严格区分大小写   
3.下划线开头的一般有特殊意义，避免使用相同的     
### 6.命名规范：   
1.模块名尽量短小，可以使用下划线分隔多个字母如 list_main  
2.包名尽量短小，并且全部使用小写字母 
3.类名单词首字母大写,例如：MyClass  
4.模块内部的类采用“_”+Pascal风格的类名组成，例如MyClass内部的类_innerMyClass  
5.一般常量的命名全部采用大写
## 第二章
### 1.基本进制
- 二进制：0b；八进制：0o；十六进制：0x；    
  1.浮点数是带有小数的，科学计数法e的规则：e前e后必有数，e前可以省略小数部分或者整数部分，e后必须为整数部分，不能出现空格； 
  2.python中的虚数使用j来表示，例如 123j就代表是一个纯虚数，而实部 使用.real，虚部 使用.imag表示，例如：
```python
x = 123+456j
print(x.real, x.imag, x) 	
```
- 在python中，不管什么类型，只要用引号引起来就是字符串，单引号、双引号和三引号皆可 	
-  '\t'的大小取决于当前制表位的空间大小，当前制表位缺几个字符填满，则\t就是几个位置，一个制表位是8个字符；	
-  切片的语法结构：对字符串的某个子串或者区间的检索称为切片，语法结构是：字符串[N:M]其中N可以省略，默认从0开始；M省略默认到结尾.	
### 2.常用的字符串操作：
1、x+y:表示将两个字符串连接起来
2、x*n:表示将字符串x复制n次
3、x in s：返回一个布尔类型的值，如果x是s的字串，返回True,否则返回False
类型转换：隐式转换和显式转换，隐式转换是在计算过程中自动转换的，例如:	
```python
x = 10
y = 3
print(x/y, end='\n\n')	
```
的结果是一个浮点型数据，就发生了隐式转换。
将字符串类型转换为int或者float时，报错的情况：字符串本身不是一个整数或者10进制数	
### 3.chr和ord函数	
chr()和ord(),是一对相反的操作，chr的作用是查找一个整数在unicode码中对应的字符是什么，ord是查找一个字符在unicode码中对应的数字是多少	
```python
print(ord('钟'), ord('翔'))
print(chr(38047), chr(32724))
```
进制之间的转换函数：十进制转十六：hex;十进制转八：oct;十进制转二：bin;	
### 4.eval函数的作用：
用于去掉字符串最外侧的引号，并按照python语句方式执行去掉引号之后的字符串；经常和input函数一起使用	
```python
age = (input("输入一个数：")) 
print(type(age))
age = eval(input("再输一次：")) 
print(type(age))
SyntaxError # 表示输入的python代码有语法错误	
```
## 第三章
### 1.算术运算符：
- \+ - * / （加减乘除，其中除得到的是float）   
- //（整除运算，得到的数取整，是int）  % (取余操作，例如10%3得到1） **（幂运算，2**3得到8）
- 运算优先级：
  - 第一级： **
  - 第二级：* / // %
  - 第三级：+ —
### 2.关于赋值操作 ：
  - python支持链式赋值，a=b=c=10 # 是合法的；
  - python还支持系列解包赋值，例如：(a,b = 10,20)；还支持字符串的分解赋值，例如:a,b,c='bed'
  - 故可以利用这样的方式直接交换，不用像C语言中还要一个额外的空间 (a,b =b,a)
  - python中的三种逻辑运算符： and not or 和C语言中&& ！ || 对应
### 3.位运算符：
1、按位 与（&）   
2、按位或（|）（与逻辑运算符差不多，先将数换算成二进制数，然后按位运算即可) 
3、按位异或（^)（数位对齐之后，如果两个位置上的数相同，那么就是0，否则为1）                
4、按位取反(~)（与逻辑取反相同）  
5、左移位(<<):将一个二进制数向左移动指定的位数，左边溢出的被丢弃，右边缺失的用0补充；  
6、右移位（>>）：是将一个二进制数向右移动指定的位数，右边溢出的被丢弃，如果该数最高位是0（表示的正数）则补充0；如果该数最高位是1（表示的负数）则补充1；
## 第四章
- 程序的描述方式：1、自然语言 2、流程图 3、伪代码 
### 1.选择结构：
```
if 表达式：
     语句块
        if 表达式：
             语句1
        else：
             语句2 
```
- python3.11中没有其他语言的switch结构，但是有一个模式匹配：match,用法和switch一摸一样
### 2.for循环结构：    
```
for 循环变量 in 遍历对象
         语句块
```
### 3.内置函数rang()
用于产生一个[n,m)的整数序列（左闭右开）,默认从0开始   
```python
for i in range(10):
    print(i,end='\t')
```
### 4.for....else循环结构：
即：如果正常结束循环，那么继续执行else语句，否则，不执行。
### 5.while循环判断四个步骤：
1）初始化变量 2）条件判断 3）语句块 4）改变变量
```
 while 表达式：
    语句块
 同理，while...else结构也可以使用
```
- break 用法和C语言基本一样  
- continue的用法和C语言基本一致 
- pass用法，是python中的保留字，意思是过，只有占位符的作用，没有任何实际意义。防止编译器报错
## 第五章
### 1.序列
是一个用于存储多个值的连续空间，每个值都对应一个整数编号，称为索引
列表、元组、集合和字典都是序列（列表、元组是有序序列； 集合和字典是无序序列）
```python
str='helloworld!'
for i in range(-11,0):   # 若要从负数开始索引，则必须左右区间都写上，0不可省略；若是从正数开始索引，则可以省略
    print(i,str[i],end='\t')
print()
```
切片操作： 是对序列的一种检索操作，检索其中的某一部分。语句是 序列[strat:end:step](仍然是一个左闭右开的区间，步长默认为1）
```python
s='helloworld'
print(s[:])
# 切片操作的步长可以为负数，意思是倒序输出，同样，检索的开始和结尾也可以为负数
```
序列可以相加，可以相乘 序列中一些常用操作：  
1、 in & not in （用来判断某个序列是否是主序列的子序列，返回值是True和False）  
2、len :计算序列的长度 max：输出序列中元素的最大值 min ：输出序列中元素的最小值     
3、s.index(x)：表示元素x在序列s中第一次出现的位置； s.count(x):表示元素x在序列s中出现的次数
### 2.列表（序列中的一种）：
1、是一系列的按特定顺序排列的元素组成 
2、是python中内置的可变序列，所谓的可变指的是，我们可以对其进行增、删、该、查  
3、在python中使用[]定义列表，元素与元素之间使用英文的逗号分隔 
4、列表中的元素可以是任意的数据类型  
5、列表还可以由List创建； 用法为 name = list();  
其中，list中的元素必须是可迭代对象数据类型（所有的序列类型都是可迭代对象），例如：  
1） 字符串 2）集合 3）字典 4）range 5）map 等，这些类型都是可迭代对象，即可以使用for...in循环遍历的
```
list.append() # 是在列表末尾添加一个元素, 它会把添加的数据当成一个整体来添加，可以是任意类型的数据类型（int型，可迭代对象，类等）
list.extend() # 与append的不同，它会把添加的数据迭代进行添加，所以它只能添加可迭代对象数据类型
# append和extend只能在末尾添加，如果要在中间添加，需要insert函数，语法：
list.insert(index,obj) # insert在插入时，也会将其看成一个整体，和append一样
```
- 列表的删除：    
  - 1、del ：可以删除某一个元素； del list[index]，也可以删除指定位置 del list[start:end:step],或者删除整个列表 del list 
  - 2、pop删除列表指定索引处的元素：list.pop(index) ,默认是删除列表最后一个元素，是一个“出栈”操作 
  - 3、remove是删除列表中某个值的元素，并且只会删除第一个和该值相等的元素 list.remove()
  - 4、clear 删除所有列表元素，list.clera()即清空所有元素
- 列表元素的修改： 
  - 可以使用list[index]对列表元素进行修改 
  - 也可以使用切片操作，对一组元素进行修改list[start:end:step],此操作可以添加元素（对空切片操作，切记不可只添加一个元素）也可以删除元素（如果指定步长，则要求元素个数和原来相同） 
  - --list.reverse()是将列表中的元素反转
  - --list.copy() 拷贝列表中的所有元素，生成一个新的列表
- 列表的遍历操作： 
  - 1、使用for..变量..in..列表 
  - 2、使用range序列，for i in range(len(list))  获取列表中的元素是：list[i]
  - 3、enumerate函数： for index,item in enumerate(list) 输出序号index和元素item，其中起始序号可以改变，即：enumerate(list,起始值)
- 列表的排序操作有两种方式： 
  - 1、列表对象的sort： list.sort(key=None,reverse=False) （默认是升序） 
  - 2、内置函数sorted():sorted(iterable,key=None,reverse=False)
- 注意：这里的key是一个函数，可以自己指定，用于自定义排序方法
- python中自定义函数主要有两种形式： 
- 1、def 
- 2、lambda:是python中的一个保留字，意思是一个匿名函数，语句为 lambda[arg1,arg2,[arg3,arg4]]:expression 
- 其中，arg是参数列表，expression由用户自定义，是一句表达式，是对前面的参数进行表达，例如：0 if a<b else 1 
  - 常见用法： add = lambda a,b: a*b，此后调用add就是在调用lambda函数 
  - 在列表排序中的应用：用作key的参数；
```python
sorted('iterable',key=lambda a:a[1],reverse=False) 
# 此句的意思是：按照lambda函数的方式排序，而lambda函数是输入参数a,返回参数a[1];
# 列表生成式：
list=['expression' for item in range]  
list=['expression' for item in range if 'condition']
# expression是要生成的元素
list=[[ _*_ for _ in range(4)] for i in range(2)] # 前面是列，后面是行
print(list)
```
'''
### 3.元组是python中内置的不可变序列
- 使用（）定义元组，元素之间使用英文的逗号分隔 
- 元组只有一个元素的时候，逗号也不能省略 
- 元组的创建方式： 
  - 1、元组名=(element1，element2)
  - 2、使用内置函数tuple: 元组名=tuple(序列）# tuple里面必须是一个序列
```python
t = tuple(tuple(range(10)))
print(t,sum(t),max(t))
```
- 元组的遍历：    
  - 1、支持切片操作 
  - 2、for ...in  操作 
  - for item in t.items():
  - 3、for i in range(len(tuple)):
  - 4、for index, item in enumerate(tuple):
- 元组生成式 
- 用t=(i for in range(5))生成的是一个生成器对象，类型不是元组、列表等，但是可以将其类型转化为对应的 
- 生成器对象可以使用__next__来取出 
- 元组和列表的区别： 1、元组是不可变的，列表是可变的； 2、元组可以作为字典的键，但列表不可以
### 4.字典类型：
是根据一个信息查找另一个信息的方式构成了“键值对”，它表示索引用的键和对应的值构成的成对关系，字典是没有索引序号的，只能靠key；    
底层逻辑是：哈希    
字典类型的创建：
- 1、直接使用{}来创建 d={key1:value1,key2:value2} 
- 2、使用内置函数：   
  1) 通过映射函数创建字典 zip(lst1,lst2)
  2) 使用函数dict(key1=value1,key2=value2)
#### 字典元素的访问和遍历：
```python
d={'hello':'H','world':'W','program':'P'}
d['hello']
d.get('hello')
```
这两者的区别是：当key不存在的时候，情况 1）会报错，而 2）会制定一个默认值，并且可以自定义默认值，例如d.get('python',10)
#### 字典元素的遍历：
```
for i/item/obj in d.items():
print(i/item.obj)
```
这样的方式遍历，这样的遍历是将字典数据类型输出为一个个的元组数据类型,字典是可变数据类型，对字典的操作：    
1) d.keys():获取所有键数据 
2) d.values()：获取所有值数据 
3) d.pop(key,default=None)：获取Key对应的值，并删除，如果没有这个key，则获取默认值 
4) d.popitem()：随机从字典取出一个key-value对（元组类型）同时将改键值对从字典删除 
5) d.clear()：清除所有的键值对
#### 字典生成式： 
d={i:random.randint(0,99) for i in range(5)} 意思是，使用range序列中的数做key，循环生成，使用randint中的随机整数做value    
第二种办法：
```python
list1=[1,2,3,4]
list2=[5,6,7,8]
d={key:value for key,value in zip(list1,list2)}
d={1:'hello',2:'world',3:''}
for i in d.items():print(i,type(i))
```
### 5.集合
- python中的集合与数学中的概念一致，是一个无序的不重复的序列
- 集合只能存储不可变数据类型，在python中集合使用{}定义
#### 创建集合的方法：
1) 直接创建s={....} // 如果创建一个空集合，则这样的方式创建的是一个字典，创建空集合得用下面的方式
2) 使用set创建，s=set(可迭代对象)，所以使用set时，可以使用集合，例如：s1=set([1,2,3,4])，因为括号内只要求是可迭代序列即可 
3) 交集：a&b：两个集合相交部分，删除重复元素 
4) 并集：a|b：两个集合全部元素，删除重复元素 
5) 差集：a-b：集合A除去和B的相交部分 
6) 补集：a^b：两个集合除去相交部分
#### 集合的操作方法：
```
s.add(x) # 添加元素X到集合
s.remove(x) # 删除元素X
s.clear(x) # 清空集合所有元素
```
#### 集合的遍历：
```
1、for item in s: 
2、for index,item in enumerate(s): # index指的是序号，不是索引，集合没有索引，所有元素都是无序的
3、生成式：s={item for item in range(10)}
```
![几种数据类型区别](D:\实验&代码\code practice\python初学\学习截图\几种数据类型区别.png)

## 第六章 
### 1、字符串 
- str.lower() 字符串全部转成小写字母，结果为新的字符串
- str.upper() 字符串全部转为大写字母，结果为新字符串
- str.split(sep=None) 字符串按照制定的分隔符sep进行分隔，结果为列表
```python
lst='cherryandtulip@163.com'
new1=lst.split('.')
new2=lst.spllit('@')
new3=lst.split()
print(new1,new2,new3)
```
- str.cont(sub) 返回sub这个字符串在str中出现的次数

- str.find(x) 查询x是否在字符串中出现，如果不存在，结果-1，存在，结果是sub首次出现的索引

- str.index(x) 与上个功能相同，区别是x不存在时，程序会报错

- str.startswith(s) 查询字符串是否以s开头 

- str.endswith(s) 查询字符串是否以s结尾

- str.replace(old,news，count) 使用news替换字符串中old字符串，count是替换次数，默认全部替换，结果为新的字符串

- str.center(width,fillchar) 字符串在指定的宽度范围内居中，可以使用fillchar填充

- str.join(item) 在item中的每个元素的后面都增加一个新的字符串str

- str.strip(chars) 从字符串中去掉左侧和右侧chars中列出的字符串，与顺序无关，只要出现就会删除

- str.lstrip(chars) 去掉左侧chars中列出的字符串

- str.rstrip(chars) 去掉右侧chars中列出的字符串

- 1.格式化字符串的三种方式 
  - 1.1 占位符 例如：%d %f %s(含义与C语言一样)	
  
    ![%占位符](D:\实验&代码\code practice\python初学\学习截图\%占位符.png)
  
  - f-string py3.6以后引入的，用{}标明被替换的字符
```python
name='zx'
age='18'
school='tk university'
print(f'姓名：{name},年龄{age},学校{school}')
```
  - str.format()
```python
name='zx'
age='18'
school='tk university'
print('姓名:{0},年龄:{1},学校:{2}').format(name,age,school)
# 这里的0，1，2 对应的是format里面参数的位置
```
![格式化字符串详细格式](D:\实验&代码\code practice\python初学\学习截图\格式化字符串详细格式.png)  
#### 字符串的编码与解码
编码：将str类型转换成bytes类型，需要使用encode
```python
str.encode(encoding='utf-8',errors='strict/ignore/replace')
#默认编码类型为utf-8
```
解码：将bytes转换成str类型
```python
bytes.decode(encoding='gbk',errors='strict/ignore/replace')
```
#### 字符串的拼接
```python
str1='hello'
str2='world'
# 第一种，使用+进行拼接
print(str1+str2)
# 第二种，使用join()函数
print(''.join([str1,str2])) # join()函数里面必须是一个可迭代对象，不能是变量，否则会报错
print('@'.join([str1,str2]))
# 第三种： 直接拼接
print('hello''world')
# 第四种 使用格式化字符串拼接
print('%s%s'%(str1,str2))
# 二、三 方式如上
```
#### 字符串的去重 
1、使用逻辑去重
```python
s="helloworldhelloworldhelloworld"
new_s=''
for item in s:
   if item not in new_s:
        new_s+=item
print(new_s)
```
2、使用集合去重
```python
s="helloworldhelloworldhelloworld"
s1=set(s) #因为集合的特性，集合中的元素是无序且不重复的，所以建立集合会自动删除重复元素
lst=list(s1)
print(lst)
lst.sort(key=s.index)
print(lst,''.join(lst))
```
### 2.正则表达式

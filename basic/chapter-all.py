#1. Python简介
#1.1 Python是什么
#Python是一种解释型语言：编写的代码会由解释器来执行。
# Python是一种高级语言，这意味着它更接近人类语言，
# 因此更容易阅读和理解。它是一种解释型语言，这意味着程序不需要编译，
# 由解释器直接执行。这让Python成为学习编程的绝佳语言，也是许多领域的首选语言。

#1.2 Python的优点
#Python简单易学，语法和结构简单明了。
#Python非常强大，拥有丰富的库和工具，可以处理几乎所有的任务。

#1.3 Python的应用领域
#Python是一种通用语言，可以应用于多种领域，如Web开发、数据科学、人工智能等。

#打印
print("Hello, world!")


#2 变量和简单数据类型
#2.1 变量
#变量是程序存储的值或数据。在Python中，变量是一个标签，用于引用存储在计算机内存中的值。变量名是程序员给变量赋予的名称，可以是任何名称，只要遵循Python的命名规则即可。
message = "Hello Python world!"
print(message)
message = "Hello Python Crash Course world!"
print(message)

#2.2 字符串
#字符串是一系列字符。在Python中，
# 用引号括起来的都是字符串，其中的引号可以是单引号，也可以是双引号。

#2.3 
#变量常被描述为可用于存储值的盒子。
"This is a string."
str1 = 'This is also a string.'


#2.3.1 使用方法修改字符串的大小写
print(str1.title())
print(str1.upper())
print(str1.lower())
print(str1)

#2.3.2 在字符串中使用变量
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + ' ' + last_name
print(full_name)

print(f"hello,{full_name.title()}!")

#  2.3.3 使用制表符或换行符来添加空白
print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#2.3.5 使用字符串时避免语法错误
message = "One of Python's strengths is its diverse community."
print(message)



# 2.4 数字
#2.4.1 整数
print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)
print(3 ** 2)
print(3 ** 3)
print(10 ** 6)
print(2 + 3 * 4)
print((2 + 3) * 4)

# 2.4.2 浮点数
print(0.1 + 0.1)
print(0.2 + 0.2)
print(2 * 0.1)
print(2 * 0.2)
print(0.2 + 0.1)
print(3 * 0.1)

# 2.4.3 整数和浮点数
print(3 / 2)
print(1 + 2.0)
print(2 * 3.0)
print(3.0 ** 2)

#2.4.4 数中的下划线
universe_age = 14_000_000_000
print(universe_age)

#2.4.5 同时给多个变量赋值
x, y, z = 0, 2, 0
print(x)
print(y)
print(z)
#2.4·6 常量
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)  
#2.5 注释
#2.5.1 如何编写注释
# Say hello to everyone.
print("Hello Python people!")
#2.5.2 该编写什么样的注释


#2.6 Python之禅
import this
#Now is better than never.
#你可以用余生来学习Python和编程的纷繁难懂之处，
# 但这样你什么项目都完不成。不要企图编写完美无缺的代码，
# 而是要先编写行之有效的代码，再决定是对其做进一步改进，
# 还是转而去编写新代码。


#3 列表简介
#3.1 什么是列表
#列表
#由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字0～9或所有家庭成员姓名的列表；也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。列表通常包含多个元素，因此给列表指定一个表示复数的名称（如letters、digits或names）是个不错的主意。
#在Python中，用方括号（[]）表示列表，并用逗号分隔其中的元素。下面是一个简单的列表示例，其中包含几种自行车：
biycycles = ['trek', 'cannondale', 'redline', 'specialized']
print(biycycles)

#3.1.1 访问列表元素
print(biycycles[0])
print(biycycles[0].title())

#3.1.2 索引从0而不是1开始
print(biycycles[1])
print(biycycles[3])
print(biycycles[-1])
print(biycycles[-2])
print(biycycles[-3])
print(biycycles[-4])

#3.1.3 使用列表中的各个值
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
myfirstbicyles = f"is a {bicycles[0].title()}."
print(myfirstbicyles)
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#3.2 修改、添加和删除元素
bicycles[2] = 'Merida'
print(bicycles)

#3.2.1 在列表中添加元素
bicycles.append('redline') #在列表末尾添加元素
print(bicycles)
bicycles.insert(2, 'Phoenix')#在列表中插入元素

#3.2.2 从列表中删除元素
print("1",bicycles)
del bicycles[2]
print(bicycles)
popped_bicycle = bicycles.pop()
print("3", bicycles)
print(popped_bicycle)
first_owned = bicycles.pop(0)
print(f"The first bicycle I owned was a {first_owned.title()}.")
print(bicycles)
bicycles.remove('cannondale')#根据值删除元素  

print(bicycles)

#3.3 组织列表
#3.3.1 使用方法sort()对列表进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()

print(cars)
cars.sort(reverse=True)#按字母顺序相反的顺序排列列表元素
print(cars)

#3.3.2 使用函数sorted()对列表进行临时排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
car_tmp = sorted(cars)
print(car_tmp)
print("\nHere is the original list:")
print(cars)

#3.3.3 倒着打印列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()#反转列表元素的排列顺序,永久性修改,只是反转列表元素的排列顺序，而不是按与字母顺序相反的顺序排列元素
print(cars)

#3.3.4 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


#3.4 使用列表时避免索引错误
motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])#IndexError: list index out of range
print(motorcycles[-1])
print(len(motorcycles))

#4 操作列表
#4.1 遍历整个列表
#需要对列表中的每个元素都执行相同的操作时，可使用Python中的for循环。
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

#4.1.1 深入地研究循环 & #4.1.2 在for循环中执行更多的操作
#循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#4.1.3 在for循环结束后执行一些操作
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

#4.2 避免缩进错误
#Python根据缩进来判断代码行与前一个代码行的关系.

#4.2.1 忘记缩进
#对于位于for语句后面且属于循环组成部分的代码行，
# 一定要缩进。如果忘记缩进， Python会提醒你:
#IndentationError: expected an indented block

#4.2.2 忘记缩进额外的代码行
#这将是一个逻辑错误。从语法上看，这些Python代码是合法的，但由于存在逻辑错误，结果并不符合预期。

#4.2.3 不必要的缩进
#如果在循环后面的代码行不需要缩进，但你不小心缩进了，Python将指出这一点。

#IndentationError: unexpected indent


#4.2.4 循环后不必要的缩进
#也是一个逻辑错误

#4.2.5 遗漏了冒号
magicians = ['alice', 'david', 'carolina']
#for magician in magicians
#    print(magician)
#SyntaxError: invalid syntax


#4.3 创建数值列表
#列表非常适合用于存储数字集合，而Python提供了很多工具，
# 可帮助你高效地处理数字列表。明白如何有效地使用这些工具后，
# 即便列表包含数百万个元素，你编写的代码也能运行得很好。

#4.3.1 使用函数range()
for value in range(1, 5):
    print(value)
#在这个示例中，range()只打印数1～4。这是编程语言中常见的差一行为的结果。
# 函数range()让Python从指定的第一个值开始数，并在到达你指定的第二个值时停止。
# 因为它在第二个值处停止，所以输出不包含该值（这里为5）。
#使用range()时，如果输出不符合预期，请尝试将指定的值加1或减1。

#4.3.2 使用range()创建数字列表
#在前一节的示例中，只是将一系列数打印出来。
# 要将这组数转换为列表，可使用list()：
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)
#使用函数range()几乎能够创建任何需要的数集。
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

#4.3.3 对数字列表执行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
#注意
#　考虑到版面，本节使用的数字列表都很短，
# 但这里介绍的知识也适用于包含数百万个数的列表。

#4.3.4 列表解析

#前面介绍的生成列表squares的方式包含三四行代码，
# 而列表解析让你只需编写一行代码就能生成这样的列表。列表解析
# 将for循环和创建新元素的代码合并成一行，并自动附加新元素。
# 面向初学者的书并非都会介绍列表解析，这里之所以介绍列表解析，
#是因为等你开始阅读他人编写的代码时，很可能会遇到它。

#使用列表解析生成前面示例中的平方数列表：
squares = [value**2 for value in range(1, 11)]
print(squares)
#要使用这种语法，首先指定一个描述性的列表名，如squares。
# 然后，指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。
# 在这个示例中，表达式为value**2，它计算平方值。
# 接下来，编写一个for循环，用于给表达式提供值，再加上右方括号。
# 在这个示例中，for循环为for value in range(1,11)，它将值1～10提供给表达式value**2。
# 请注意，这里的for语句末尾没有冒号。

#4.4 使用列表的一部分
#在第3章中，你学习了如何访问单个列表元素。
# 在本章中，你一直在学习如何处理列表的所有元素。
# 你还可以处理列表的部分元素，Python称之为切片

#4.4.1 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])#不包含索引4的元素
print(players[:4])
print(players[2:])
print(players[-3:])

#4.4.2 遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player)

#4.4.3 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#4.5 元组
#列表非常适合用于存储在程序运行期间可能变化的数据集。
# 列表是可以修改的，这对处理网站的用户列表或游戏中的角色列表至关重要。
# 然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。
# Python将不能修改的值称为不可变的，而不可变的列表被称为元组。

#4.5.1 定义元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#dimensions[0] = 20 #TypeError: 'tuple' object does not support item assignment
#print(dimensions)

#4.5.2 遍历元组中的所有值
for dimension in dimensions:
    print(dimension)

#4.5.3 修改元组变量
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print(dimensions)
for dimension in dimensions:
    print(dimension)
    #首先定义一个元组，并将其存储的尺寸打印出来（见❶）。
    # 接下来，将一个新元组关联到变量dimensions（见❷）。
    # 然后，打印新的尺寸（见❸）。
    # 这次，Python不会引发任何错误，因为给元组变量重新赋值是合法的：

#5 if语句

#5.1 一个简单示例
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#5.2 条件测试
#每条if语句的核心都是一个值为True或False的表达式，这种表达式称为条件测试。

#5.2.1 检查是否相等
car = 'bmw'
if car == 'bmw':
    print(True)

#5.2.2 检查是否相等时不考虑大小写
car = 'Audi'
print(car.lower() == 'audi')
print(car)

#5.2.3 检查是否不相等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#5.2.4 比较数字
age = 18
if age == 18:
    print(True)
if age != 19:
    print(True)
if age < 21:
    print(True)
if age <= 21:
    print(True)
if age > 21:
    print(True)
if age >= 21:
    print(True)

#5.2.5 检查多个条件
age_0 = 22
age_1 = 18
if age_0 >= 21 and age_1 >= 21:
    print(True)
age_3 = 22
if age_0 >= 21 and age_1 >= 21 and age_3 >= 21:
    print(True)
if age_0 >= 21 or age_1 >= 21:
    print(True)
if age_0 >= 21 or age_1 >= 21 or age_3 >= 21:
    print(True)

#5.2.6 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print(True)
if 'pepperoni' in requested_toppings:
    print(True)
if 'mushrooms' not in requested_toppings:
    print(True)

#5.2.7 布尔表达式
game_active = True
can_edit = False

#5.3 if语句
#5.3.1 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
#5.3.2 if-else语句
age = 17
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#5.3.3 if-elif-else结构 && #5.3.4 使用多个elif代码块
age = 19
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
elif age < 22:
    print("Your admission cost is $10.")
else:
    print("Your admission cost is $15.")

#5.3.5 省略else代码块
age = 17
if age < 4:
    price = 0
elif age < 18:
    price = 5
print(f"Your admission cost is ${price}.")

#5.3.6 测试多个条件
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#5.4 使用if语句处理列表
#5.4.1 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#5.4.2 确定列表不是空的
requested_toppings = [] #先判断是否为空
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"5.4.2 Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

#5.4.3 使用多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"5.4.3 Adding {requested_topping}.")
    else:
        print(f"5.4.3 Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")



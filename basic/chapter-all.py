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


#6 字典
#在Python中，字典是一系列键值对。
# 每个键都与一个值相关联，你可使用键来访问相关联的值。
# 与键相关联的值可以是数、字符串、列表乃至字典。
#事实上，可将任何Python对象用作字典中的值。
#6.1 一个简单的字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#6.2 使用字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
alien_0['color'] = 'yellow'
print(alien_0['color'])

alien_0['x_position']= 0
print(alien_0)
alien_0['y_position'] = 25
print(alien_0)

#6.2.1 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color'])

#6.2.2 添加键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#6.2.3 先创建一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

#6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
alien_0['color'] = ''

print(alien_0)



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])

#6.2.5 删除键值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']

print(alien_0)

#6.2.6 由类似对象组成的字典

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

#6.2.7 使用get()获取字典中的值
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])#KeyError: 'points'
#Traceback (most recent call last):
#  File "/Users/hwgeng/Documents/PythonCrashCoursePracitce/basic/chapter-all.py", line 602, in <module>
#    print(alien_0['points'])#KeyError: 'points'
#KeyError: 'points'


point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


#6.3 遍历字典
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():#items()返回一个键-值对列表,声明两个变量，用于存储键值对中的键和值
    print(f"\nKey: {key}")
    print(f"Value: {value}")

#6.3.2 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys():#提取字典favorite_languages中的所有键，并依次将它们赋给变量name
    print(name.title())

#6.2.9 按顺序遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
#遍历字典时，会默认遍历所有的键。因此，如果将上述代码中的：
for name in favorite_languages:
    print(name.title())
#替换为：
for name in favorite_languages.keys():
    print(f"{name.title()}, thank you for taking the poll.")
#输出将不变

#6.3.4 遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
#这种做法提取字典中所有的值，而没有考虑是否重复。
# 涉及的值很少时，这也许不是问题，但如果被调查者很多，
# 最终的列表可能包含大量重复项。为剔除重复项，可使用集合（set）。
# 集合中的每个元素都必须是独一无二的：

for language in set(favorite_languages.values()):
    print(language.title())

#注意:
#可使用一对花括号直接创建集合，并在其中用逗号分隔元素：
languages = {'python', 'ruby', 'python', 'c'}
for language in languages:
    print(language.title())
print(languages)

#6.4 嵌套
#有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。

#6.4.1 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

import random
#自动生成aliens
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': random.randint(1, 100), 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}")

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
print(aliens[:5])

#6.4.2 在字典中存储列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
#6.4.3 在字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
#在前面的示例中，字典users 包含两个键：'aeinstein' 和'mcurie'。

#7 用户输入和while循环

#7.1.1 编写清晰的程序
#message = input("pls input your name:")
#print("hello ",message, ", nice to meet you!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
#name = input(prompt)
#print(f"\nHello, {name}!")

#7.1.2 使用int()来获取数值输入
#age = input("How old are you? ")
#age = int(age)
#print(age)


#7.1.3 求模运算符
print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)
#求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
number = random.randint(1, 100)
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


#7.2 while循环简介

#7.2.1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

#7.2.2 让用户选择何时退出
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
#while message != 'quit':
    #message = input(prompt)
    #if message != 'quit':
    #    print(message)


#7.2.3 使用标志
active = True
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

#7.2.4 使用break退出循环
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\n(Enter 'quit' when you are finished.)"
#while True:
#    city = input(prompt)
#    if city == 'quit':
#        break
#    else:
#        print(f"I'd love to go to {city.title()}!")


#7.2.5 在循环中使用continue

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

#7.3 使用while循环来处理列表和字典

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#7.3.2 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)    

#7.3.3 使用用户输入来填充字典
responses = {}

# while name != 'quit':
#     name = input('input your name: ')
#     if name == 'quit':
#         break
#     resp = input('input your respons: ')
#     responses[name] = resp
# print(responses)

 # 设置一个标志，指出调查是否继续。  
# polling_active = True  
# while polling_active:      # 提示输入被调查者的名字和回答。
#     name = input("\nWhat is your name? ")      
#     response = input("Which mountain would you like to climbsomeday? ")      # 将回答存储在字典中
#     responses[name] = response      # 看看是否还有人要参与调查。
#     repeat = input("Would you like to let another person respond? (yes/ no) ") 
#     if repeat == 'no':          
#         polling_active = False  # 调查结束，显示结果。  
# print("\n--- Poll Results ---") 
# for name, response in responses.items():      
    # print(f"{name} would like to climb {response}.")


#8 函数

#8.1 定义函数
def greet_user():
    print("hello")

greet_user()


def greet_user(username):
    print(f"Hello, {username.title()}!")
greet_user('jesse')

#8.1.2 实参和形参
#在函数greet_user()的定义中，变量username是一个形参——函数完成其工作所需的一项信息。
# 在代码greet_user('jesse')中，值'jesse'是一个实参。实参是调用函数时传递给函数的信息。

#8.2 传递实参
#函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。
#向函数传递实参的方式有很多，包括位置实参、关键字实参、还可以使用列表和字典。

#8.2.1 位置实参

#调用函数时，Python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
# 为此，最简单的关联方式是基于实参的顺序。这种关联方式称为位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet('dogy', 'huazi')

describe_pet(animal_type='hamster', pet_name='harry')

#8.2.3 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")
#这里修改了函数describe_pet()的定义，
# 在其中给形参animal_type指定了默认值'dog'。这样，调用这个函数时，
# 如果没有给animal_type指定值，Python就将把这个形参设置为'dog'：
describe_pet('willie')

#8.2.4 等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")

    # 一条名为Willie的小狗。
describe_pet('willie')
describe_pet(pet_name='willie')# 一只名为Harry的仓鼠。'
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

#8.2.5 避免实参错误
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type.title() + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')
#describe_pet()#TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

#8.3 返回值
#8.3.1 简单的返回值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#8.3.2 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'hooker')
print(musician)

musician = get_formatted_name('john', 'hooker', 'h')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john', 'hooker')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#8.3.3 返回字典
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', 3)
print(musician)


#8.3.4 结合使用函数和while循环
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# while True:
#     print("\nPlease tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("Hello, " + formatted_name)

#8.4 传递列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg) 
names = ['hannah', 'ty', 'margot']
greet_users(names)
#8.4.1 在函数中修改列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
compited_models = []
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
print_models(unprinted_designs, compited_models)
print(compited_models)

#重新组织代码
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#   8.4.2 禁止函数修改列表
#要将列表的副本传递给函数，可以像下面这样做：
def function_name(list_name):
    """对列表进行修改"""
    print(list_name)
    list_name.append(6)
    print(list_name)

list_name_ = [1,2,3,4,5] 
function_name(list_name_[:])#切片表示法[:]创建列表的副本
print(list_name_)

#8.5 传递任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese', 4)

#8.5.1 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#8.5.2 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的用户的所有信息"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert','einstein', location='princeton', field='physics')
print(user_profile)

#8.6 将函数存储在模块中
# 使用函数的优点之一是可将代码块与主程序分离。
# 通过给函数指定描述性名称，可让主程序容易理解得多。
# 你还可以更进一步，将函数存储在称为模块
# 的独立文件中，再将模块导入
# 到主程序中。import语句允许在当前运行的程序文件中使用模块中的代码。

#8.6.1 导入整个模块
import pizza as pz
pz.make_pizza_m(16,'pepperoni')
pz.make_pizza_m(12,'mushrooms','green peppers','extra cheese')


#8.6.2 导入模块中的特定函数
from pizza import plus_
print(plus_(2,3))
from pizza import make_pizza_m as mp
mp(16,'pepperoni')

#8.6.3 使用as给  函数  指定别名

from pizza import plus_ as pz2 #函数plus_()的别名pz2
print(pz2(2,3))

#8.6.4 使用as给模块指定别名
import pizza as p
p.make_pizza_m(16,'pepperoni')
p.make_pizza_m(12,'mushrooms','green peppers','extra cheese')

#8.6.5 导入模块中的所有函数
from pizza import *
print(plus_(2,9))
make_pizza_m(16,'pepperoni')

#8.7 函数编写指南
#应给函数指定描述性名称，且只在其中使用小写字母和下划线。
#每个函数都应包含简要地阐述其功能的注释。
#该注释应紧跟在函数定义后面，并采用文档字符串格式。
#PEP 8建议代码行的长度不要超过79字符，这样只要编辑器窗口适中，就能看到整行代码。

# 如果形参很多，导致函数定义的长度超过了79字符，
# 可在函数定义中输入左括号后按回车键，并在下一行按两次Tab键，
# 从而将形参列表和只缩进一层的函数体区分开来。
def abc(
        safdsf,
        asdfas,
        asfasfg,
        gsagaeg
        ):
    print(safdsf)


#9 创建和使用类
#使用类几乎可以模拟任何东西。
import dog as d
my_dog = d.Dog('willie',6)

# 9.1 创建一个类

# 9.1.1 定义一个类
#9.1.2 根据类创建实例
import dog as d
my_dog = d.Dog('willie',6)
#访问属性
print(my_dog.name) 
print(my_dog.age)
#调用方法
my_dog.sit()
my_dog.roll_over()

#9.2 使用类和实例

import car as c
#9.2.2 给属性指定默认值
my_new_car = c.Car('audi','a4',2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#9.2.3 修改属性的值

my_new_car.odometer_reading = 55
my_new_car.read_odometer()

#通过方法修改属性的值
my_new_car.update_odometer(66)
my_new_car.read_odometer()
my_new_car.update_odometer(55)
my_new_car.read_odometer()

#通过方法对属性的值进行递增
my_old_car = c.Car('subaru','outback',2013)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()
my_old_car.increment_odometer(100)
my_old_car.read_odometer()



#9.3 继承
'''编写类时，并非总是要从空白开始。
如果要编写的类是另一个现成类的特殊版本，
可使用继承。一个类继承另一个类时，将自动获得另一个类的所有属性和方法。
原有的类称为父类，而新类称为子类'''

my_tesla = c.ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()

#9.4.5 导入模块中的所有类
'''
要导入模块中的每个类，可使用下面的语法：
from module_name import *
不推荐使用这种导入方式，原因有二。
第一，如果只看文件开头的import语句，就能清楚地知道程序使用了哪些类，将大有裨益。
然而这种导入方式没有明确地指出使用了模块中的哪些类。
第二，这种方式还可能引发名称方面的迷惑。
如果不小心导入了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。
这里之所以介绍这种导入方式，是因为虽然不推荐使用，但你可能在别人编写的代码中见到它。
'''

#9.6 类编码风格
'''
    类名应采用驼峰命名法
，即将类名中的每个单词的首字母都大写，而不使用下划线。
实例名和模块名都采用小写格式，并在单词之间加上下划线。
对于每个类，都应紧跟在类定义后面包含一个文档字符串。
这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
可使用空行来组织代码，但不要滥用。在类中，可使用一个空行来分隔方法；
而在模块中，可使用两个空行来分隔类。
需要同时导入标准库中的模块和你编写的模块时，
先编写导入标准库模块的import语句，再添加一个空行，
然后编写导入你自己编写的模块的import语句。
在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何处。
'''


#10 文件和异常
"""
将学习处理文件，让程序能够快速地分析大量数据；
你将学习错误处理，避免程序在面对意外情形时崩溃；
你将学习异常，它们是Python创建的特殊对象，
用于管理程序运行时出现的错误；
你还将学习模块json，它让你能够保存用户数据，
以免在程序停止运行后丢失。
"""

#10.1.1 读取整个文件
import os
print(os.getcwd())

with open('basic/pi_digits.txt') as file_object:
    contents = file_object.read()
#    print(contents)

print(contents.rstrip())

#10.1.2 文件路径
file_path = 'basic/pi_digits.txt'#变量filename表示的并非实际文件——它只是一个让Python知道到哪里去查找文件的字符串
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
#10.1.3 逐行读取
with open(file_path) as file_object:
    for line in file_object:
        print(line)
        #print(line.rstrip())
#10.1.4 创建一个包含文件各行内容的列表
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#10.1.5 使用文件的内容
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(len(pi_string))

#10.1.6 包含一千万位的大型文件
#对于可处理的数据量，Python没有任何限制。
# 只要系统的内存足够多，你想处理多少数据都可以。
file_path = 'basic/pi_million_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
    for line in lines:
        pi_string += line.strip()
#print(f"{pi_string[:52]}...")
#birthday = "20990101"
birthday = "48955897"
if birthday in pi_string:
    print("Your birthday appears in the first ten million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


#10.2 写入文件

file_path = 'basic/programming.txt'
with open(file_path, 'a') as file_object: #a表示附加模式, w表示写入模式, r表示读取模式, r+表示读取和写入模式
    contents = file_object.write('I love programming.')
with open(file_path) as file_object:
    c2 = file_object.read()
    print(c2)

#10.3 异常
#Python使用称为异常的特殊对象来管理程序执行期间发生的错误。

#10.3.1 处理ZeroDivisionError异常
#print(5/0)#ZeroDivisionError: division by zero

#10.3.2 使用try-except代码块
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

#10.3.3 使用异常避免崩溃 #10.3.4 else代码块
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)
   
#10.3.5 处理FileNotFoundError异常
filename = 'alice.txt'
try:
    with open(filename) as f_obj:
        contents = f_obj.read()
        print(contents)
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")

#10.3.6 分析文本
file_path = 'basic/alice.txt'
try :
    with open(file_path) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()#split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中
    num_words = len(words)
    print(f"The file {file_path} has about {num_words} words.")

#10.3.7 使用多个文件
#《悉达多》《白鲸》《小妇人》
filenames = ['sidao.txt', 'baijun.txt', 'xiaowomen.txt']
for filename in filenames:
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#10.3.8 静默失败
def count_words(filename):
    """计算一个文件里有多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass#pass语句让Python什么都不要做，即可避免在文件不存在时引发异常
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

#10.3.9 决定报告哪个错误
#Python的错误处理结构让你能够细致地控制与用户分享错误信息的程度，要分享多少信息由你决定。

#10.4 存储数据

#很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。不管关注点是什么，程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，几乎总是要保存他们提供的信息。一种简单的方式是使用模块json来存储数据。

#10.4.1 使用json.dump()和json.load()

import json
numbers = [2,3,5,7,11,13]
filename = 'basic/numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
    numbers = json.load(f_obj)
print(numbers)

#10.4.2 保存和读取用户生成的数据
import json
#username = input("What is your name? ")
username = "Hali "
filename = 'basic/username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + "!")
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    print("Sorry, the file " + filename +"does not exist.")
else:
    print("Welcome back, "+ username + " !")

#10.4.3 重构
"""
你经常会遇到这样的情况：代码能够正确地运行，
但通过将其划分为一系列完成具体工作的函数，还可以改进。
这样的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。
"""

def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("we'll remember you when you come back, " + username + "!")

greet_user()
# 一、 print

# 1. 打印， 单引号与双引号都可以
print("Hello World")

# 2. 拼接字符串
print("Hello" + " World" + "!")

# 3. 如果字符串有多个引号一起使用,可以让单双引号互相嵌套或者是使用转义字符
print("My 'Name' Is Zgc")
print('My "Name" Is Zgc')
print("My \"Name\'s\" Zgc")

# 4. 换行， 不允许直接换行， 但可以使用 \n 来换行
print("Hello \nWorld")

# 5. 三引号跨行字符串，三个单引号或者双引号可以实现换行
print("""忽有狂徒夜磨刀，
帝星飘摇荧惑高!""")

# 二、变量
# 变量只能由数字，字母，下划线组成， 且不能由数字开头
# 变量名大小写敏感
# 变量名不要占用关键字
name = 'zgc'
print("您好，" + name)

# 三、写一个计算一元二次方程的公式
# import 最好放在文件的最上面
import math

a = -1
b = 2
c = 3
delta = b ** 2 - 4 * a * c
print((-b + math.sqrt(delta)) / (2 * a))
print((-b - math.sqrt(delta)) / (2 * a))

# 四、注释 -- #
# 1. 快捷键 Ctrl + /

# 2. 多行注释
""" 
    我是
    多行
    注释
"""
# 五、类型的判断方法以及获取字符串长度的方法
# 1. NoneType
"""
在Python 中，有一个特殊的常量None（N 必须大写）。 
它表示没有值，也就是空值，可以看到，它属于 NoneType 类型。
"""
type1 = None
print(type(type1))  # <class 'NoneType'>

# 2. str
type2 = 'hello ,\nzgc'
print(type(type2), len(type2), type2[1])  # <class 'str'> 11 e
# 获取字符串的最后一位
print(type2[len(type2) - 1])  # c

# 格式化字符串
# str.format(a,b,c)方法， {数字}表示会用format的第几个参数进行替换
a = '月'
b = '上'
msg = """
床前明{0}光，疑是地{1}霜。
举头望明{0}，低头思故乡。
""".format(a, b)
print('msg:', msg)

# str.format(x=a,y=b)方法，key可以与value取同一个名称
msg1 = """
床前明{x}光，疑是地{y}霜。
举头望明{x}，低头思故乡。
""".format(y=b, x=a)
print('msg1:', msg1)

# f"{变量}"
msg2 = f"""
床前明{a}光，疑是地{b}霜。
举头望明{a}，低头思故乡。
"""
print('msg2:', msg2)

# 3. bool
# True False 要大写
type3 = True
print(type(type3))  # <class 'bool'>

# 4. number
type4 = 3
type5 = 5.0
print(type(type4), type(type5))  # <class 'int'> <class 'float'>

# 六、input
# input 函数的返回值为用户输入的结果， 类型是字符串
# user_age = input("您的年龄是：")
# print("您今年" + user_age + "岁了!", type(user_age))  # 您今年34岁了! <class 'str'>

# 七、计算BMI
# BMI = 体重 /（身高 ** 2）
"""
int: 将一个字符串或数字转换为整型;
float: 将整数和字符串转换成浮点数;
str: 将对象或者数字转换为字符串
"""
# user_weight = input('请输入您的体重（单位kg）：')
# user_height = input('请输入您的身高（单位m）：')
#
# user_BMI = float(user_weight) / (float(user_height) ** 2)
# print("您的BMI为：" + str(user_BMI))

# 八、条件语句
# 1. 基本使用
# mood_index = int(input("对象今天的心情指数是："))
# if mood_index >= 60:
#     print("今晚可以打游戏")
#     print("去吧，皮卡丘")
# elif 40 < mood_index < 60:
#     print("今晚不能打游戏")
# else:
#     print("节哀")

# 2. 条件嵌套
# num = int(input("输入一个数字："))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 2 和 3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num % 3 == 0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")

# 九、逻辑运算
x = 10
y = 20
"""
and: 表达式：x and y,	如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值. 
or:  表达式：x or y, 如果 x 是 True，它返回 x的值，否则它返回 y 的计算值.
not: 表达式：not x, 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True. 
"""
print(x and y)  # 20
print(x or y)  # 10
print(not (x and y))  # False

# 十、列表
shopping_list = ['笔记本', '手机', 'ipad']
print(shopping_list, type(shopping_list))  # <class 'list'>

# 末尾添加元素
shopping_list.append('显示器')
print(shopping_list, len(shopping_list))  # 4

# 删除列表元素
shopping_list.remove('手机')
print(shopping_list, shopping_list[0])

# 修过数组元素
shopping_list[1] = '键盘'
print(shopping_list)

# 打印最大、最小值，排序列表
test_list = [1, 5, 6, 34, 2345, 2]
print(max(test_list))
print(min(test_list))
print(sorted(test_list))

# 十一、 字典
"""
键必须是唯一的，但值则不必;
值可以取任何数据类型，但键必须是不可变的;
不可变类型：字符串、整数、浮点数、布尔类型、元组...
可变类型：列表、字典...
dict 作为 Python 的关键字和内置函数，字典名不建议命名为 dict;
"""

obj = {
    ('张伟', 23): '1311111111',
    ('张伟', 36): '15000000000',
    '李莉': '13777777777',
    5: 49
}
# 打印字典， 字典长度， 字典类型
print(obj, len(obj), type(obj))  # 3 <class 'dict'>

# 查看字典属性 obj[键名]
print(obj['李莉'], obj[('张伟', 36)], obj[5])

# 添加属性
obj['妹子'] = '999999999'
print(obj)

# 更新已有属性
obj['妹子'] = '888888888'
print(obj)

# 查看某个键是否存在于字典中

print('小明' in obj)  # False
print(('张伟', 23) in obj)  # True

# 删除键值对

del obj['妹子']
del obj[5]
print(obj)

# 十二、for循环
# 可以对字符串、列表、元组、集合、字典等数据类型进行迭代
"""
for 变量名 in 可迭代对象:
    ...
    操作
    ...
"""

temp_list = [36.6, 36.7, 37.3, 38, 37.8, 37.5, 36.9]

for person_temp in temp_list:
    if person_temp >= 37.3:
        print('你阳了', person_temp)
    else:
        print('你没阳', person_temp)

temp_dict = {'001': 36.6, '002': 38.4, '003': 37.5}

# 得到字典所有的键名
print(temp_dict.keys())
# 得到字典所有的键值
print(temp_dict.values())
# 得到字典所有的键值对
print(temp_dict.items())
# dict_items([('001', 36.6), ('002', 38.4), ('003', 37.5)])

for person_id, person_temp in temp_dict.items():
    if person_temp >= 37.3:
        print(person_id)

# :.2f保留几位浮点数
for person_id, person_temp in temp_dict.items():
    print("编号为{0}的用户您好，您当前的体温为：{1:.2f}".format(person_id, person_temp))
    print(f"编号为{person_id}的用户您好，您当前的体温为：{person_temp:.3f}")

# for 配合 range 使用
# range(起始值, 结束值（不包含在内）, 步长（一次跨越几个值）)
#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)

for number in range(1, 20, 3):
    print(number)

# 计算 1-100 的和
total_num = 0
for i in range(1, 101):
    total_num += i

print('total_num:', total_num)

# 十三、while循环
"""
while 判断条件(condition)：
    执行语句(statements)
    ……
"""

a = 1
while a < 10:
    print(a)
    a = a + 2

# 计算 1-100 的和
n = 100
total_num = 0
initial = 1
while initial <= n:
    total_num = total_num + initial
    initial += 1

print('total_num:', total_num)

# 用while实现求数字平均值
# total_num = 0
# count = 0
# print('哈喽呀! 我是一个求平均值的程序。')
# user_input = input('请输入数字（完成所有数字输入后，请输入q终止程序）：')
#
# while user_input != 'q':
#     total_num += float(user_input)
#     count += 1
#     user_input = input('请输入数字（完成所有数字输入后，请输入q终止程序）：')
#
# if count == 0:
#     result = 0
# else:
#     result = total_num / count
# print('数字平均值为：', result)

# 十四、函数
# 函数的定义规则：
"""
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""


# 定义函数
def print_fn(string):
    """函数_文档字符串: 打印任何传入的字符串"""
    print(string)
    return


# 调用函数
print_fn("我要调用用户自定义函数!")
print_fn("再次调用同一函数")

"""
python 函数的参数传递：
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
"""
x = 2
y = [1, 2, 3]


def change_int(a):
    a = 10


def change_list(a):
    a.append(4)


change_int(x)
change_list(y)

print(x, y)  # 2 [1, 2, 3, 4]

# 十五、import导入模块

# 直接引入模块：import 模块名
# import statistics

# 使用：模块名.函数名/变量名
# statistics.mean()

# 按需引入：from 模块名 import 函数名/变量名
from statistics import mean, median


# 使用:
# mean()
# median()

# 全部引入： from 模块名 import *
# from statistics import *
# 使用:
# mean()
# median()

# 十六、Class
class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print('喵' * self.age)

    def think(self, content):
        print(f"{self.name}思考{content}")


cat1 = Cat('巧克力', 3, '黑色')
cat2 = Cat('香子兰', 5, '白色')

print('cat1', f"名字是{cat1.name}，年龄是{cat1.age}岁，颜色为{cat1.color}")
cat1.speak()
cat2.speak()

cat1.think('去抓沙发')
cat2.think('去抓纸箱')


# 定义一个学生类
# 1. 属性包含学生姓名、学号、以及语数英三科成绩
# 2. 能够设置学生的某科目成绩
# 3. 能打印出该学生的所有科目成绩

class Student:
    def __init__(self, name, stu_id):
        self.name = name
        self.stu_id = stu_id
        self.grades = {'语文': 0, '数学': 0, '英语': 0}

    def set_grade(self, course, score):
        if course in self.grades:
            self.grades[course] = score

    def print_grades(self):
        print(f"学生：{self.name}(学号：{self.stu_id})的成绩为:")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")


stu1 = Student('zgc', '001')
print(stu1.grades)
stu1.set_grade('数学', 88)
stu1.set_grade('语文', 98)
stu1.set_grade('英语', 66)
print(stu1.grades)
stu1.print_grades()


# 类的继承
# class 子类名(父类名)

# 父类：员工类
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工姓名：{self.name}，员工工号：{self.id}")


#  子类：全职员工
class FullTimeEmployee(Employee):
    def __init__(self, name, id, salary):
        # 子类调用父类构造方法
        super().__init__(name, id)
        self.salary = salary

    def calculate_monthly_pay(self):
        print(self.salary)


# 子类： 兼职员工
class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        result = self.work_days * self.daily_salary
        print(result)


user1 = FullTimeEmployee('张三', '001', 8888)
user2 = PartTimeEmployee('李四', '002', 200, 15)

user1.print_info()
user2.print_info()

user1.calculate_monthly_pay()
user2.calculate_monthly_pay()

# 十七、文件操作
# 打开文件: open(文件路径, 模式, 编码模式)
# 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法
f = open('data.txt', 'r', encoding='utf-8')
content = f.read()
print(content)
f.close()

print(["192.168.1.%d" % x for x in range(1, 255)])

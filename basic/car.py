#9.2.1 Car类 
class Car:
        """一次模拟汽车的简单尝试"""
        def __init__(self, make, model, year):
                """初始化描述汽车的属性"""
                self.make = make
                self.model = model
                self.year = year
                self.odometer_reading = 0
        def get_descriptive_name(self):
                """返回整洁的描述性信息"""
                long_name = str(self.year) + ' ' + self.make + ' ' + self.model
                return long_name.title()
        def read_odometer(self):
                """打印一条指出汽车里程的消息"""
                print(f"This car has {self.odometer_reading} miles on it.")
        def update_odometer(self, mileage):
                """
                将里程表读数设置为指定的值
                禁止将里程表读数往回调
                """
                if mileage >= self.odometer_reading:
                        self.odometer_reading = mileage
                else:
                        print("You can't roll back an odometer!")
        def increment_odometer(self, miles):
                """将里程表读数增加指定的量"""
                self.odometer_reading += miles
        def fill_gas_tank(self):
                """给汽车加gas"""
                print("This car needs gas!")

class Battery:
        """模拟电动汽车电瓶的简单尝试"""
        def __init__(self, battery_size=75):
                """初始化电瓶的属性"""
                self.battery_size = battery_size
        def describe_battery(self):
                """打印一条描述电瓶容量的消息"""
                print("This car has a " + str(self.battery_size) + "-kWh battery.")
        def get_range(self):
                """打印一条消息，指出电瓶的续航里程"""
                if self.battery_size == 75:
                        range = 260
                elif self.battery_size == 100:
                        range = 315
                print("This car can go about " + str(range) + " miles on a full charge.")
        def upgrade_battery(self):
                """升级电池"""
                if self.battery_size != 100:
                        self.battery_size = 100
                        print("Upgraded the battery to 100 kWh.")
                else:
                        print("The battery is already upgraded.")

#9.3.1 子类的方法__init__()
"""
创建子类时，父类必须包含在当前文件中，且位于子类前面。
"""
class ElectricCar(Car):#定义子类时，必须在圆括号内指定父类的名称。
        """电动汽车的独特之处"""
        def __init__(self, make, model, year):
                """初始化父类的属性"""
                '''super()是一个特殊函数，让你能够调用父类的方法。
                这行代码让Python调用Car类的方法__init__()，
                让ElectricCar实例包含这个方法中定义的所有属性。
                父类也称为超类（superclass），名称super由此而来。'''
                super().__init__(make, model, year)#方法__init__()接受创建Car实例所需的信息
                self.battery_size = 75
                self.battery = Battery()#将实例用作属性
        def describe_battery(self):
                """打印一条描述电瓶容量的消息"""
                print(f"This car has a {self.battery_size}-kWh battery.")
        def fill_gas_tank(self):
                """电动汽车没有油箱"""
                print("This car doesn't need a gas tank!")

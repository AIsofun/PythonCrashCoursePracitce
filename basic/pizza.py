def plus_(a, b):
    return a + b

#8.6.1 导入整个模块
def make_pizza_m(size, *toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
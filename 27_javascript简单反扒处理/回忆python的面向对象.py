# 类型, 对某一种数据类型的封装
class Person:  # 原型对象
    # 构建了这个对象...构造方法.. 有瑕疵.不影响你理解
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def chi(self):  # 这东西叫方法
        print(self.name, "人会吃")

    def play(self):
        print("xxx")

p1 = Person("alex", 18)   # 实例对象
p2 = Person("wusir", 28)
p1.chi()  # 对象能执行什么取决于类中定义了什么
p2.chi()

print(p1.__class__)

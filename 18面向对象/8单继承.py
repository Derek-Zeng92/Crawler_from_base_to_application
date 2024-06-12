class A:
    money = 10000
    def speak(self):
        print('我有很多钱', self.money)

# B类继承A类
class B(A):
    money = 20000
    # def run(self):
    #     print('我跑的特别快，比狗还快，在被狗追的时候')
    # 对于父类中的speak方法进行重写
    # 调用父类中的方法
    def speak(self):
        # super().speak()  # 重新调用父类的方法speak
        A.speak(self)  # 重新调用父类的方法speak
        # 补充自己的想法
        print('我是b中的speak')
b = B()
print(b.money)
print(b.speak())
# b.run()
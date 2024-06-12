class Test:
    # 属性
    name = 'lucky'
    age = 18
    # 方法
    # self是由当前对象自动传参
    def speak(self):
        print('self', self)
        # 内部调用属性和方法使用self
        print('self', self.name)
        print('self', self.age)
        print('lucky is a good man')
        return 'lucky'
t = Test()
# 调用Test类中的name属性
print(t.name)
print(t.age)
print(t.speak())
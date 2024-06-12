class Test:
    # 属性
    name = 'lucky'
    age = 18
    # 方法
    # self是由当前对象自动传参
    def speak(self, sex):
        print('lucky is a good man', sex)

# t = Test()
# 调用Test类中的name属性
# print(t.speak('man'))
# 调用不存在的属性或方法报错
# print(t.sex)
# t1 = Test()
# t2 = Test()
# t1.sex = 'man'  # 给t1对象添加一个属性 sex
# print(t1.sex)
# print(t2.sex)

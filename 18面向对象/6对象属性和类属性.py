class Test:
    # 属性
    # 类属性name
    name = 'lucky'
    age = 18
    # 方法
    # self是由当前对象自动传参
    def speak(self, sex=1):
        self.aa = 'zhangsan'
        print('lucky is a good man', sex)

t = Test()
t.speak()
# print(t.__dict__)
# print(Test.__dict__)
# Test.aa
t.aa
# t.name = 'zhangsan'
# 创建对象属性name  调用的时候优先调用对象属性  如果对象中没有 则找类中的
# 如果类中也没有  则报错
# print(t.name)
# print(t.__dict__)
# print(Test.__dict__)
# t2 = Test()
# print(t2.name)
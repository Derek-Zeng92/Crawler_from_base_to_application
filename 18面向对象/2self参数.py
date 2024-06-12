class Test:
    # 属性
    name = 'lucky'
    age = 18
    # 方法
    def speak(self):
        print('lucky is a good man')
        return 'lucky'
t = Test()
# 调用Test类中的name属性
# print(t.name)
print(t.speak())

# import requests
# session = requests.Session()
# session.get()
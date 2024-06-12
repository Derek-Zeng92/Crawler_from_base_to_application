# import pymysql
# pymysql.Connect(host='127.0.0.1', user='root')

class Test:
    name = 'lucky'
    # 初始化当前对象的
    # 可以在实例化的时候 自动传递一些参数
    def __init__(self, host, port, user):
        self.host = host   # 对象属性
        self.port = port
        self.user = user
        sex = 'w'   # 局部变量 只有当前函数内部可以使用 就是正常的函数的局部变量
        print(host,port,user)


t = Test(host='127.0.0.1', port=3306, user='root')
# print(t.__dict__)
# Test.aaa = 'aaa'  # 类属性
# print(Test.__dict__)
# print(t.sex)
# print(Test.sex)
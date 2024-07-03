# # def func():
# #     pass
# #
# #
# # a = 1
# # b = 2
# # # 你才是主人. 你想要什么就搞什么
#
# # 规划： 这一类的东西能干什么
# 类究竟是什么?
# 类：类型，相同类型的数据。 应该有相同的操作
class NvPengYou:
    def __init__(self, shengao, tizhong, id, address):  # 初始化-在创建该类的对象时。 给对象进行自动初始化
        self.身高 = shengao
        self.体重 = tizhong
        self.身份证 = id
        self.住址 = address
        self.性别 = "女"  # 不是所有的参数必须得是穿过来的。
    # 类中声明的函数. 叫方法
    # self 表示当前这个对象
    def nakele(self):
        print("1.先蹦起来")
        print("2.跳个舞")
        print("3.扭扭捏捏走到冰箱处")
        print("4.甩给老子一瓶可乐")

    def happy(self):
        # self就是当前正在执行这个方法的对象
        # print(self)  # self:  对象.方法()  -> self就是对象
        # 打印在哪里happy, 我想去女朋友的住所 happy
        print(self.住址, "去happy")

    def fei(self):
        print("飞上万米高空")

linzhiling = NvPengYou(185, 135, 10086, "美丽富饶的沙河")
linzhiling.happy()

# canglaoshi = NvPengYou()
# canglaoshi.happy()
# # canglaoshi.shengao=165
# # canglaoshi.tizhogn = 155
# # canglaoshi.id=10010
# # canglaoshi.address = "美丽富饶的巩华城"

# 你想执行xxxx操作. 先看类型.


class Fu:
    def zhuanqian(self):
        print("会赚钱")


class Zi(Fu):  # 继承父类, 子类自动拥有父类中, 出了私有内容外的其他所有东西
    pass

class Sun(Fu):
    pass

zi = Zi()
zi.zhuanqian()

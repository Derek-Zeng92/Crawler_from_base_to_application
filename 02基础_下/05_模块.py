
# # 导入 模块  模块名就是文件名或者文件夹名
import jiamijie as jj  # 自动的把jiamijie.py运行。在内存中产生一个独立的内存

print("爬取东西")
print("需要解密")
jj.jiemi()
print("ok了")
jj.jiami()

# 另一种导入方式, 具体需要什么功能就导入什么功能
from jiamijie import jiami, jiemi
from jiamijie1 import jiami as j1  # 当名字冲突的时候可以用as区分
from jiamijie2 import jiami as j2

jiami()
jiemi()

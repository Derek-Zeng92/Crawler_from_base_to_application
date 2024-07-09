# 需要安装pyexecjs ->  pip install pyexecjs
# 在python中连接CMD的那个东西是subprocess里面的Popen

# 解决execjs的乱码问题.
# 在引入execjs之前. 加上以下代码
import subprocess
from functools import partial  # 作用.用来锁定某个参数的固定值
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs  # -> 其实用的是nodejs

print(execjs.get().name)  # 打印引擎名字.

# 调用my.js中的fn函数
f = open("my.js", mode="r", encoding="utf-8")
all_js_code = f.read()
# 加载js
js = execjs.compile(all_js_code)
# 调用函数
r = js.call("fn", "哈哈", "呵呵", "吼吼")  # fn(1,2,3)
print(r)



import subprocess
from functools import partial  # 作用.用来锁定某个参数的固定值
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

s = """{
        "name": "alex",
        "age": 18,
        hunfou: false,
        chou: true,
        address: "黑龙江",
        hobby:[]
    }
"""

# # 想办法往 -> json身上靠.
# # 前端的eval
d = execjs.eval(s)
print(d)
print(type(d))

import time
import math
import random

data = ""
for i in range(8):
    v1 = math.ceil(16 * random.uniform(0, 1))
    v2 = hex(v1)[2:].upper()
    data += v2
result = data.rjust(8, "0")

e = int(time.time() * 1000)
t = hex(e)[2:].upper()

b_lsid = "{}_{}".format(result, t)
print(b_lsid)

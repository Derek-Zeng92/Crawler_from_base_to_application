fn = 72
e = 43
for d in range(1, fn):
    if d * e % fn == 1:
        print(d)


# 加密过程:
m = 71
# 公钥
n = 91
e = 43

c = m ** e % n
print(c)  # 85  ???

# n的取值: 很大的数
# e的取值: 不会很大

c = 85
# 解密过程
n = 91
d = 67

print((c**d) % n)  # 71




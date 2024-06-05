i = 0
def sum1():
    global i
    for x in range(10000000):
        i += x
        i -= x
    print('sum1', i)

def sum2():
    global i
    for x in range(10000000):
        i += x
        i -= x
    print('sum2', i)
sum1()
sum2()
print(i)
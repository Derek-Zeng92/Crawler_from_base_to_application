import threading

name = 'lucky'

def run():
    global name
    name = '马冬梅'
    age = 18
    print(f'我叫:{name} 我今年{age}岁了')

thr = threading.Thread(target=run)
thr.start()
thr.join()
# run()
print('我在外部获取数据', name)
print('over')

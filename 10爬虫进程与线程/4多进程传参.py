from multiprocessing import Process

# def run1(num, name):
def run1(num, name='lucky'):
    for i in range(num):
        print(f'我是{name}函数')
        # 当前代码阻塞在这了  卡在这了

if __name__ == '__main__':
    # 注意 传递参数如果为一个值  则需给,
    # TypeError: 'int' object is not iterable
    # TypeError: 'int' object is not iterable
    # 元祖的效率高于列表
    Process(target=run1, args=(1,)).start()
    # Process(target=run1, args=[1]).start()
    # Process(target=run1, args=(1, )).start()
    # Process(target=run1, args=(1, 'lucky')).start()
    # for i in 1:
    #     pass
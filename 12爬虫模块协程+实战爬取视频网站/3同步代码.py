import time

def run(index):
    print("lucky is a good man", index)
    time.sleep(2)
    print("lucky is a nice man", index)

for i in range(1, 5):
    run(i)
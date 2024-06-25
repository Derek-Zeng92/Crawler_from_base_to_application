import traceback
def func():
    print(1/0)

try:
    print(1)
    func()
    print(2)
except Exception as e:
    print(e)
    print(traceback.format_exc())

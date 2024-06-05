import _thread
import win32api


def run():
    win32api.MessageBox(0, 'Lucky is a good man', '666我的大宝贝', 6)


_thread.start_new_thread(run, ())
print('over')
while True:
    pass
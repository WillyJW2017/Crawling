import threading
import time

def hello(index):
    print('Hello World --- %d' %index)
    time.sleep(2)

def line_thread():
    for i in range(5):
        hello(i)

def mul_thread():
    for i in range(10):
        th = threading.Thread(target=hello, args=[i])
        th.start()

if __name__ == '__main__':
    # line_thread()
    mul_thread()
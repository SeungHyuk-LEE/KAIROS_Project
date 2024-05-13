import threading
import time

def camMain(arg) :
    while True:
        if arg == 1:
            time.sleep(2)     # 2초 기다림
            print('camMain - arg 1')

        elif arg == 2:
            time.sleep(4)     # 3초 기다림
            print('camMain - arg 2')

camThread = threading.Thread(target=camMain, args=(1,))
camThread.start()


camThread = threading.Thread(target=camMain, args=(2,))
camThread.start()

while True:
    time.sleep(3)     # 3초 기다림
    print('main')

'''
使用类中的new实现的单例，支持多线程单例
'''


import threading
import time 

class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        time.sleep(1)

    def __new__(cls,*args,**kwargs):
        if not hasattr(Singleton,'_instance'):
            with Singleton._instance_lock:
                if not hasattr(Singleton,'_instance'):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print('obj1={},obj2={}'.format(obj1,obj2))

def task(args):
    obj =Singleton()
    print("obj",obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()
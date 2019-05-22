'''
使用装饰器实现单例
'''
def Singleton(cls):
    _instance = {}

    def _singleton(*args,**kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args,**kwargs)
        return _instance[cls]
    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self,x=0):
        self.x = x
    

a1 = A(2)
a2 = A(3)

print(a1,a2)
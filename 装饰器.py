""" 装饰器 """
import time


def taketime(func):
    def take(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("耗时 %.2f s" % (end - start))

    return take


class Foo(object):
    # def __init__(self, var=0):
        # self.var = var

    @taketime
    def foo(self, x):
        print('executing foo(%s,%s)' % (self, x))
        print('self->', self)

    @classmethod
    def class_foo(cls, x):
        print('executing class_foo(%s,%s)' % (cls, x))
        print('cls->', cls)

    @staticmethod
    def static_foo(x):
        print('executing static_foo(%s)' % x)

    @taketime
    def show(self):
        print("我是被装饰的函数")
        time.sleep(3)

    # @property
    # def var(self):
    #     return self._var


footest = Foo()
print(footest.foo(1), footest.class_foo(2), footest.static_foo(3))
# k = Foo.var
footest.show()
# print(k)

import time

def deco01(func):
    def wrapper(*args,**kwargs):
        print("deco01开始执行")
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("deco01执行完成,耗时%.2f"%(end-start))
    return wrapper

def deco02(func):
    def wrapper(*args,**kwargs):
        print("deco02开始执行")
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("deco02执行完成,耗时%.2f" % (end - start))
    return wrapper

@deco02
@deco01
def pow_method(x,n=10):
    assert isinstance(x,(float,int))
    print("开始计算{}的{}次方".format(x,n))
    value = pow(x,n)
    print(value)
    print("计算完毕")

pow_method(pow(2,9),10)


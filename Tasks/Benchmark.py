import time
def func(y): 
    time.sleep(4)    
    return y ** 2

def brenchmark(func):
    def newFunc(*arg,**kwargs):
        x = time.time()
        result = func(*arg,**kwargs)
        x1 = time.time()
        print( x1 - x )
        return result 
    return newFunc

print(brenchmark(func)(2))
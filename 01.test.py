def rapper(fn):
    def inner():
        print("我是装饰器")
        fn()    # fn就代表func函数
    return inner

@rapper
def func():
    print('我是被装饰的')
func()


# map([lambda x:x*i for i in range(4)])
g = lambda x,y:x+y
print(g([1,2,3],[4,5,6]))



map(lambda x:x**2,[1,2,3])

def square(x):
    return x**2
print(map(square,[1,2,3]))

i = 'lisi'
a = eval('i')
print(a)


import logging

# logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] \
#                     - %(levelname)s: %(message)s',filename='log.txt',filemode='w')
# logging.debug('这是⼀个debug级别的⽇志信息')
# logging.info('这是⼀个info级别的⽇志信息')
# logging.warning('这是⼀个warning级别的⽇志信息')
# logging.error('这是⼀个error级别的⽇志信息')
# logging.critical('这是⼀个critical级别的⽇志信息')

# logging.basicConfig(level=logging.DEBUG,
# format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',filename="log.txt",filemode="w")
# logging.debug('这是⼀个debug级别的⽇志信息')
# logging.info('这是⼀个info级别的⽇志信息')
# logging.warning('这是⼀个warning级别的⽇志信息')
# logging.error('这是⼀个error级别的⽇志信息')
# logging.critical('这是⼀个critical级别的⽇志信息')

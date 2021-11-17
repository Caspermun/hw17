def decor(func):
    def wrapper(arg):
        print('Hello')
        func(arg)
        print('Bye')
    return wrapper

@decor
def multiply(a):
    a = a**2
    print(a)

multiply(11111)
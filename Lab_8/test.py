def func(x):
    def func2(y):
        return x * y
    return func2


print(func(2)(3))

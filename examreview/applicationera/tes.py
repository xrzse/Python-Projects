def foo(x):
    x[0] = x[0] + 1
    return x
a = [0]*10
print(a[0])
b = foo(a)
print(a[0],b[0])
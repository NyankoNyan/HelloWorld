class Test:
    pass
a = Test()
a.arg = 2

Test.ext = None

def another():
    pass

another.arg = 10

another()
print(another)
print(another.arg)
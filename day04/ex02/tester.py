from callLimit import callLimit
@callLimit(3)
def f():
    print ("f()")
@callLimit(1)
def g():
    print ("g()")
for i in range(3):
    f()
    g()


# def my_docorator(a: int):
#     def test(function):
#         def wrapper():
#             print("hello first", a)
#             function()
#             print("hello second", a)
#         return wrapper
#     return test



# @my_docorator(1)
# def trash():
#     print("trash")

# trash()


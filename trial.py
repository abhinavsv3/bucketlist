

class MyClass:
  """ Simple Class """
  i = 5
  g = fun
  def __init__(self):
    print "Constructor Called"
  def f(self):
    return "Hello World"


def fun():
   print "Test"

y = MyClass()
print "Here " + str(y.i)
y.i= 10
print "y 2 " + str(y.i)
z = MyClass()
print z.i
print "I am Here"
z = y.f()
print z

fun()
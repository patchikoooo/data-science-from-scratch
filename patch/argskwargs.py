def doubler(f):
	def g(*args, **kwargs):
		return 2 * f(*args, *kwargs)
	return g

def func1(x):
	return x + 1

g = doubler(func1)
print(g(3))

def f2(x, y):
	return x+y

g = doubler(f2)
print(g(1, 2))
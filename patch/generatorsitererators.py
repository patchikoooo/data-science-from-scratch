def lazy_range(n)
	'''a lazy version of range'''
	i = 0
	while i < n:
		yield i
		i += 1

'''
	dict.items() = returns a list
	dict.iteritems() = returns an iterator
'''
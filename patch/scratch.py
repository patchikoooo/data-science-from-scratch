list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))

x = list(enumerate(list1))
print(x)

index, letters = zip(*x)
print(index)
print(letters)


import random
#random = random.random()
four_uniform_randoms = [random.random() for _ in range(4)]
print(four_uniform_randoms)


### Reproducing random results
#random.seed(10)
print(random.random()) # 0.5714025946899135
#random.seed(10)
print(random.random()) # 0.5714025946899135
print(random.random()) # 0.4288890546751146

### Choosing randomly from a range
print(random.randrange(6)) # [0, 1, 2, 3, 4, 5]
print(random.randrange(3, 6)) # [3, 4, 5]

### random shuffle
my_numbers = list(range(10))
random.shuffle(my_numbers)
print('random.shuffle:')
print(my_numbers)

### random.choice --> randomly selects in a list
myfriends = ['Yui', 'Patch', 'Ryan']
# my_best_friend = random.choice(myfriends)
# print(random.choice())
# sample without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
print('random.sample()')
print(winning_numbers)
### identify who the “key connectors” are among data scientists.

import pprint
#from __future__ import division

pp = pprint.PrettyPrinter(indent=4)

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
(4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]['friends'].append(users[j])
    users[j]['friends'].append(users[i])

#pp.pprint(users)
#print(users[0])

def number_of_friends(user):
    # How many friends does_user_have?
    return len(user['friends'])

total_connections = sum(number_of_friends(user) for user in users)
avg_connections = total_connections / len(users)


# print(number_of_friends(users[0]))
print(avg_connections)

# create a list(user_id, number_of_friends)
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
print(num_friends_by_id)

# x = sorted(num_friends_by_id, key=lambda (user_id, num_friends): num_friends,reverse=True)
def sortlist(inputtuple):
    return inputtuple[1]

x = sorted(num_friends_by_id, key=sortlist, reverse=True)
print(x)


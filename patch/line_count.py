# for every line passed into the script
#import egrep

import sys
# And here's one that counts the lines it receives and then writes
#		out the count:

count = 0
for line in sys.stdin:
	count += 1

print(count)
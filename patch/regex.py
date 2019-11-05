import re

'''
	1. re.match('a', 'cat')		--> returns True if 2nd argument
				starts with the regular expression, else
				returns False
	2. re.search(regex, string) --> returns generator of the match
	3. re.split(regex, string) 	--> splits the strings by the regex match
				returns a list
	4. re.sub(regex, replacement, string) --> returns a text with a substituted
				value using the regex
'''

print(re.sub("R(.)D(.)", r'\1-\2', "R2D2"))
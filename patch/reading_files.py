# The basic of text files

# 'r' means read-only
file_for_reading = open('most_common_words.py', 'r')

# 'w' is write-will destroy the file if it already exists!
file_for_writing = open('most_common_words.py', 'w')

# 'a' is for append-for adding to the end of the file
file_for_appending = open('most_common_words.py', 'a')

# dont forget to cloose your files when you're done
file_for_writing.close()


# Because it is easy to forget to close your files, you should
#		always use them in a with block, at the end of which they
#		will be closed automatically

with open(filename, 'r') as f:
	data = function_that_gets_data_from(f)

# at this point f has already been closed, so don't try to use it
assert process(data)


# If you need to read a whole text file, you can iterate over the
#	lines of the file using for:
with open('input.txt', 'r') as f:
	for line in file:		# look at each line in the file
		if re.match("^#", line):	# use a regex to see if it starts with '#'
			starts_with_hash += 1


# Every line you get this way ends in a newline char,
# so you'll often want to strip() if before doing anything with it

def get_domain(email_address):
	# split on '@' and return the last piece
	return email_address.lower().split("@")[-1]

with open('email_address.txt', 'r') as f:
	domain_counts = Counter(get_domain(line.strip())
							for line in f
							if "@" in line)
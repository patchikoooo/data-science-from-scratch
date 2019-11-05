from collections import defaultdict, Counter
import pprint

pp = pprint.PrettyPrinter(indent=4)

'''
As a data scientist, you know that you also might enjoy meeting users with similar
interests. (This is a good example of the “substantive expertise” aspect of data science.)
After asking around, you manage to get your hands on this data, as a list of pairs
(user_id, interest):
'''

interests = [
(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
(0, "Spark"), (0, "Storm"), (0, "Cassandra"),
(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
(1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
(2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),
(4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
(5, "Haskell"), (5, "programming languages"), (6, "statistics"),
(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
(7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
(8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
(9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
	return [user_id for user_id, user_interest in interests if user_interest == target_interest]

print(data_scientists_who_like('Hadoop'))

interests_by_user_id = defaultdict(list)



for user_id, interest in interests:
	interests_by_user_id[user_id].append(interest)

pp.pprint(interests_by_user_id)

# returning the hash version
words_and_counts = Counter(interest.lower() for user, interest in interests)
print(words_and_counts)
print("\n\n")

# returning the tupled-list version
print(words_and_counts.most_common())


'''
defaultdict
	-> creates a normal dictionary
	-> if you try to look up a key that it does not contains,
			it first add a value with a zero-argument funtction
			you provided when you created it

Counter
	-> turns a sequence of values into a defaultdict(int)-like
			object mapping keys to counts.
	-> We will primarily use this in making histograms
	-> .most_common() -> sort the Counter result from most-common
			to least common
					  -> Passing an argument, .most_common(3) will
			return the first 3 values of the sorted data
'''

'''
Sets
	-> represents a collection of distinct elements
	-> use for two main reasons.
			1. Very fast operation on sets
			2. If we have a large collection of items that we want
					to use for amembership test, a set is more appropriate than a list
	-> In data science, we will be using sets more than
			dictionaries and sets
'''

mylist = [1, 2, 3, 4, 1, 1, 2, 3, 2, 1]
print(set(mylist)) # returns {1, 2, 3, 4}

hundreds_of_other_words = ['adfasd',' adf', 'the','you','are','me','on','the']
stopwords_list = ['a', 'an', 'at'] + hundreds_of_other_words + ['yet', 'you']
stopwords_set = set(stopwords_list)
"zip" in stopwords_list # False, but have to check every element
"zip" in stopwords_set # very fast to check

print('Sorting')
#print(stopwords_list.sort(key=lambda (word, count): word, reverse=True)
print(sorted(words_and_counts.most_common(), key=lambda word: word[0], reverse=True))
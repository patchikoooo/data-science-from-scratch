import re
import pandas as pd
import numpy
import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter(indent=4)

'''
data set containing each user’s salary (in
dollars) and tenure as a data scientist (in years):
'''
def p(forprint):
	pp.pprint(forprint)

def tenure_bucket(tenure):
	if tenure < 2:
		return "less than two"
	elif tenure < 5:
		return "between two and five"
	else:
		return "more than 5"
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
	(48000, 0.7), (76000, 6),
	(69000, 6.5), (76000, 7.5),
	(60000, 2.5), (83000, 10),
	(48000, 1.9), (63000, 4.2)
]

# keys are years, values are lists of the salaries for each tenure
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	salary_by_tenure[tenure].append(salary)

#pp.pprint(salary_by_tenure)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
	tenure: sum(salaries) / len(salaries)
	for tenure, salaries in salary_by_tenure.items()
}

#p(average_salary_by_tenure)

# keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
	salary_by_tenure_bucket[tenure_bucket(tenure)].append(salary)

p(salary_by_tenure_bucket)

average_salary_by_tenure_bucket = {
	tenure: (sum(salaries) / len(salaries))
	for tenure, salaries in salary_by_tenure_bucket.items()
}

p(average_salary_by_tenure_bucket)
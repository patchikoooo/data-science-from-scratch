from bs4 import BeautifulSoup
import requests

html = requests.get("http://example.com/").text
soup = BeautifulSoup(html, 'html5lib')


#first_paragraph = soup.find('p')
# Get the first paragraph
print(soup.p)

# first_paragraph_text
print()
print(soup.p.text)

#first paragraph words
print()
print(soup.p.text.split())

# extract tag's by treating it like a dict
try:
	print(soup.p['class'])		# raises KeyError if didn't found
except KeyError:
	print("didn't found the tag")
print(soup.a.get('href'))	# returns none if didn't found
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif w.title() in data:
		return data[w.title()]
	elif w.upper() in data:
		return data[w.upper()]
	elif len(get_close_matches(w, data.keys())) > 0:
		answer = input("Did you mean '%s' instead ? Type 'Y' for yes and 'N' for no : " % get_close_matches(w, data.keys())[0])
		while answer != 'Y' and answer != 'N' and answer != 'y' and answer != 'n':
			answer = input("Type 'Y' for yes and 'N' for no : ")
		if answer == 'Y' or answer == 'y':
			return data[get_close_matches(w, data.keys())[0]]
		elif answer == 'N' or answer == 'n':
			return "The word doesn't exist, please double check it."
	else:
		return "The word doesn't exist, please double check it."

word = input("Input the word you are looking for : ")
output = translate(word)

if type(output) == list:
	for item in output:
		print(item)

else:
	print(output)

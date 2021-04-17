import json

data = json.load(open("data.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	else:
		return "The word doesn't exist, please double check it."

word = input("Input the word you are looking for : ")
print(translate(word))

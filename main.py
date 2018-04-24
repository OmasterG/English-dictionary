import json
from difflib import get_close_matches
from difflib import SequenceMatcher

data = json.load(open("data.json"))

def search_dict(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:          # to take care of proper nouns, since they start with Capital letters. mecca will be read as Mecca.
        return (data[word.title()])
    elif word.upper() in data:
        return data[word.upper()]       # Handles acronyms. responds to words like USA, NATO.
    elif len(get_close_matches(word,data.keys(), cutoff=0.8)) > 0:
        yn = input("Incorrect word.Did you mean %s? Enter Y for yes and N for no:" % get_close_matches(word, data.keys(), cutoff=0.8)[0])
        if yn == "Y" or  yn == "y":
            print("we are in Y")
            return (data[get_close_matches(word,data.keys(),cutoff=0.8)[0]])
        elif yn == "N" or yn == "n":
            print("we are in N")
            return ("The word does not exist. check the spelling!")
        else:
            return("I do not know what this option means")
    else:
        return ("The word does not exist. check the spelling!")

while True:
    word = input("enter the word: ")
    output = (search_dict(word))
    if type(output) == list:
        for o in output:
            print(o)
    else:
        print (output)

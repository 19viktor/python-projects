import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json",'r'))

def int_dictionary(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        closematch = get_close_matches(word, data.keys())[0]
        answer = input("Did you mean " + closematch + '? Enter y if yes and n if no')
        if answer.lower() == 'y':
            return data[closematch]
        elif answer.lower() =='n':
            return "That word does not exist in this dictionary."
        else:
            return "We did not understand your entry"
    else:
        return "That word does not exist in this dictionary."

word = input("What word would you like the definition of?")

definition = int_dictionary(word)

if type(definition) ==list:
    for item in definition:
        print(item)
else:
    #means that it has to be a string
    print(definition)




"""
This is the brute force way of doing it without special functions and such.
this would go in the 'else' block in this case.

answer = ""
likelyword = ""
highratio = 0
for w in data:
    ratio = difflib.SequenceMatcher(None,word,w).ratio()
    if ratio > 0.7:
            if ratio > highratio:
                highratio = ratio
                likelyword = w
    if likelyword != "":
        answer = input("Did you mean " + likelyword + "? Type yes if you did")
    if answer == "yes":
        return data[likelyword]

    else:
        return "That word does not exist in this dictionary."
"""

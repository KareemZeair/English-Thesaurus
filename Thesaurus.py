
import json
from difflib import get_close_matches

data = json.load(open("Application 1 English Thesaurus\data.json"))


def translate(w):
    w = w.lower()

    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif w.upper() in data:
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        reply = input("Do you mean %s?\nEnter Y if yes or N if no:" %
                      get_close_matches(w, data.keys())[0])

        if reply == "Y" or reply == "y":
            return data[get_close_matches(w, data.keys())[0]]

        elif reply == "N" or reply == "n":
            return "Word does not exist! Please double check it."

        else:
            return "Invalid entry!"

    else:
        return "Word does not exist! Please double check it."


word = input("Enter word: ")
output = translate(word)
i = 1

if type(output) == list:
    for item in output:
        print("Definition: %s-%s" % (i, item))
        i += 1
else:
    print(output)

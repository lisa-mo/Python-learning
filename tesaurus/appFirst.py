import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        select_option = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if select_option.lower() == "y" or select_option.lower() == "yes":
            return data[get_close_matches(word, data.keys())[0]]
        elif select_option.lower() == "n" or select_option.lower() == "no":
            if word.title() in data:
                return data[word.title()]
            elif word.upper() in data:
                return data[word.upper()]
            else:
                return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

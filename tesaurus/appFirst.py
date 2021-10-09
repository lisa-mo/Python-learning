import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(sample_word):
    check_word = sample_word.lower()
    if check_word in data:
        return data[check_word]
    elif check_word.title() in data:
        return data[check_word.title()]
    elif check_word.upper() in data:
        return data[check_word.upper()]
    elif len(get_close_matches(check_word, data.keys())) > 0:
        select_option = input("Did you mean "f"'{get_close_matches(check_word, data.keys())[0]}' instead? "
                              f"Enter Y if yes, or N if no: ")
        if select_option.lower() == "y" or select_option.lower() == "yes":
            return data[get_close_matches(check_word, data.keys())[0]]
        elif select_option.lower() == "n" or select_option.lower() == "no":
            if check_word.title() in data:
                return data[check_word.title()]
            elif check_word.upper() in data:
                return data[check_word.upper()]
            else:
                return "The check_word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The check_word doesn't exist. Please double check it."


word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

import re
import PyDictionary
from PyDictionary import PyDictionary

dictionary = PyDictionary()

def get_syn(word):
    print(dictionary.synonym(word))

# API key: f1578022-3504-4512-bd10-4c6aeef2267f
# browser link: https://dictionaryapi.com/api/v3/references/ithesaurus/json/test?key=f1578022-3504-4512-bd10-4c6aeef2267f
# make requirements file for requests package

# work on parsing cover letter - overly repeated words

def count_words(text, dict):
    words = re.split(r"[;,.?! \t\n]+", text)
    for word in words:
        if word in dict:
            dict[word] = dict[word] +1
        else:
            dict[word] = 1
    for key in list(dict.keys()):
        if dict[key] > 4:
            print(key, ":", dict[key])






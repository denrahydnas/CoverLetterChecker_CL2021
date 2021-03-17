import re
import PyDictionary
from PyDictionary import PyDictionary
from keyword_manip import *

dictionary = PyDictionary()


# work on parsing cover letter - overly repeated words
def count_words(text, dict, new_list):
    words = re.split(r"[;,.?! \t\n]+", text)
    for word in words:
        if word in dict:
            dict[word] = dict[word] +1
        else:
            dict[word] = 1
    for key in list(dict.keys()):
        if dict[key] > 3 and (len(key)) > 5:
            print("you used the word '{}' {} times.".format(key, dict[key]))
            new_list.append(key)


#get synonyms from PyDictionary for repeated words

def get_syn(word):
    return(dictionary.synonym(word))

def get_syns(list):
    ranger = len(list)
    for i in range(ranger):
        find_syn = get_syn(list[i])
        print(list[i], ":", find_syn[0:5])




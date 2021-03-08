from keyword_manip import *


#create keyword list class to capture keywords from job listing - esp __iter__

class KeyList:
    def __init__(self, k_list = None):
        self.k_list = k_list

    def __len__(self):
        return len(self.k_list)

    def add(self, new_word):
        self.k_list.append(new_word)
    
    def create_keylist(self, text):
        k_list = []
        for i in range(len(key_list)):
            if key_list[i] in text:
                k_list.append(key_list[i])
    










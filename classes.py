import re

#add keyword not in list to list fro future reference
#from Treehouse class Python I/O

keyword_file = open("keywords.txt")
keyword_list = keyword_file.readlines()
keyword_file.close()



#create keyword list class to capture keywords from job listing
class KeyList:
    def __init__(self, k_list = None):
        self.k_list = k_list

    def __len__(self):
        return len(self.k_list)

    def add(self, new_word):
        self.k_list.append(new_word)
    
    def create_keylist(self, text):
        k_list = []
        for i in range(len(keyword_list)):
            if keyword_list[i] in text:
                k_list.append(keyword_list[i])
    










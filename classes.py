import re

#add keyword not in list to list fro future reference
#from Treehouse class Python I/O

keyword_file = open("keywords.txt")
keyword_list = keyword_file.read()
keyword_file.close()


#create keyword list class to capture keywords from job listing
class KeyList:
    def __init__(self, k_list = None):
        self.k_list = k_list

    def __len__(self):
        return len(self.k_list)

    @classmethod
    def create_keylist(cls, job_text):
        k_list = []
        for keyword in job_text:
            if re.search(keyword, keyword_list) == True:
                k_list.append(KeyList(keyword))
        return cls(k_list)


        










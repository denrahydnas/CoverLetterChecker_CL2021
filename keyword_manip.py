import re

# create master key list from txt file
key_list = []
with open("keywords.txt") as file:
    for line in file:
        phrase = line.strip('\t\n')
        key_list.append(phrase)

# eventually get this from user input:
job_text = "I want to learn more about product design and on-boarding UX through the software development life cycle"

# reuseable list parsing function - should this be a class eventually?
# req inputs are: 
# 1) list to compare  2) text to compare 3) empty list to store results
refined_list = []
def list_parser(list1, text, list2):
    list_len = len(list1)
    for i in range(list_len):
        if list1[i] in text:
            list2.append(list1[i])


# testing: list_parser(key_list, job_text, refined_list)
# testing: print(refined_list)
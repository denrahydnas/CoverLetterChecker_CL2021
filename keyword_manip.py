import re

#create master key list from txt file
key_list = []

def list_maker():
    with open("keywords.txt") as file:
        for line in file:
            phrase = line.strip('\t\n')
            key_list.append(phrase)

list_maker()
list_len = (len(key_list))

# eventually get this from user input:
job_text = "I want to learn more about product design and on-boarding UX through the software development life cycle"

#loop to check if phrases are in user text
for i in range(list_len):
    word = key_list[i]
    if word in job_text:
        print(word)
    

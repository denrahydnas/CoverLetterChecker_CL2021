import re

# create master key list from txt file

master_list = []
with open("keywords.txt") as file:
    for line in file:
        phrase = line.strip('\t\n')
        master_list.append(phrase)

#get path from user to find .txt file to compare to Keyword list

def try_file():
    while True:
        path_name = input("\nPlease save the job listing as a .txt file and enter the path here: ")
        try:
            if path_name[-4:] == ".txt":
                with open (path_name) as userfile:
                    file = userfile.read()
                    return file
            else:
                print("This is not the correct file type.")
        except OSError:
            print("OS Error: We were not able to open your file.")
            print("Please double check that the name and file type are correct.")


# refine lists to sort matches

def find_matches(list1, text, list2):
    '''req inputs are: 1) list to compare  2) text/list to compare 3) empty list to store results'''
    ranger = len(list1)
    for i in range(ranger):
        if list1[i] in text:
            list2.append(list1[i])

def unused_list(list1, list2, new_list):
    '''req inputs are: 1) list to compare  2) text/list to compare 3) empty list to store results'''
    ranger = len(list1)
    for i in range(ranger):
        if list1[i] not in list2:
            new_list.append(list1[i])

# work on parsing cover letter - check for repeated word usage, sentences starting with I

def split_words(text, new_list):
    words = re.split(r"[;,.?! \t\n]+", text)
    new_list.append(words)

def split_sentences(text, new_list):
    sentences = re.split(r"[.?!\t\n]+", text)
    new_list.append(sentences)


       

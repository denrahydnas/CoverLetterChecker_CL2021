# create master key list from txt file
key_list = []
with open("keywords.txt") as file:
    for line in file:
        phrase = line.strip('\t\n')
        key_list.append(phrase)

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

# reuseable list parsing function - should this be a class eventually?
# req inputs are: 
# 1) list to compare  2) text to compare 3) empty list to store results

#refined_list = []

def list_parser(list1, text, list2):
    list_len = len(list1)
    for i in range(list_len):
        if list1[i] in text:
            list2.append(list1[i])

def unused_list(list1, list2, new_list):
    ranger = len(list1)
    for i in range(ranger):
        if list1[i] not in list2:
            new_list.append(list1[i])

# testing
#file = get_user_file(path_name)
#list_parser(key_list, file, refined_list)
#print(refined_list)
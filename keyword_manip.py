
# create master key list from txt file
key_list = []
with open("keywords.txt") as file:
    for line in file:
        phrase = line.strip('\t\n')
        key_list.append(phrase)

#get path from user to find .txt file to compare to Keyword list

def get_user_file(path_name):
    if path_name[-4:] == ".txt":
        with open (path_name) as userfile:
            file = userfile.read()
        return file
    else:
        path_name = input("Please save the file as .txt and paste the path here:  ")

# reuseable list parsing function - should this be a class eventually?
# req inputs are: 
# 1) list to compare  2) text to compare 3) empty list to store results

refined_list = []

def list_parser(list1, text, list2):
    list_len = len(list1)
    for i in range(list_len):
        if list1[i] in text:
            list2.append(list1[i])


# testing
#file = get_user_file(path_name)
#list_parser(key_list, file, refined_list)
#print(refined_list)
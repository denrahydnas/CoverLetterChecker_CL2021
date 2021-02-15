#add keyword not in list to list fro future reference
#from Treehouse class Python I/O

def add_keyword(word):
    file = open("keywords.txt", "a")
    file.write(word+"\n")

add = input("would you like to add a Keyword to your search? Yes/No   ")

if add.upper() == "YES":
    add_keyword(input("Please type the Keyword here:   "))
else:
    print("No worries, thanks!")
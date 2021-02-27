from classes import KeyList
from keyword_manip import list_parser


# Have User input Job Listing text 
# disregard cases
# compare job listing to keyword list, create sub list (class???)
# count keys found
# print found_keyword list for User
# ask user to add missing keywords
# maybe - have user add .txt versions of job listing/cover letter/resume instead of copy/paste?
# compare found_keyword list to cover letter/ resume
# return matches

key_list = []
with open("keywords.txt") as file:
    for line in file:
        phrase = line.strip('\t\n')
        key_list.append(phrase)

#introduction

print('*'*80)
print("Welcome to my Job Application Keyword Checker.") 
print("Upload the listing for the job you are applying to and check it against our list of over 1,000 keywords.")
print("Then, compare your list to your cover letter or resume to make sure you've implememted as many keywords as possible.")
print("You can also check for a few more cover letter tips to help your application make it past the HR AI and increase the chances of the hiring staff seeing your application.  ")
print("Please type QUIT or Q at any time to exit")
print('*'*80)

while True:
    answer = input("Would you like to check for keywords? Yes/No:   ")
    if answer.upper() == "Q":
        break
    if answer.upper() == "QUIT":
        break
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        try:
            listing_text = input("Please paste the text from the job listing here:     ")
        except ValueError:
            print("That's not a valid response. Please try again.")

# clean listing text before parsing - bullet points are causing exit out of program
# better to use text file rather than user input??

    new_list = []
    list_parser(key_list, listing_text, new_list)
    print("We have identified {} keywords from your job listing. ".format(len(new_list)))
    answer = input("Would you like to review the list? Yes/No   ")
    if answer.upper() == "Q":
        break
    if answer.upper() == "QUIT":
        break
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        print(new_list)
    else:
        break
    
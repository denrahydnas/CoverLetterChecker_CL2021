from classes import *
from keyword_manip import *


#introduction

print('*'*80)
print('\n')
print("Welcome to my Job Application Keyword Checker.") 
print("Upload the listing for the job you are applying to and check it against our list of over 1,000 keywords.")
print("Then, compare your list to your cover letter or resume to make sure you've implememted as many keywords as possible.")
print("You can also check for a few more cover letter tips to help your application make it past the HR AI and increase the chances of the hiring staff seeing your application.  ")
print('\n')
print('*'*80)

# While loop for program

while True:
    answer = input("Would you like to check for keywords? Yes/No:   ")
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        try:
            listing_text = input("Please save the job listing as a .txt file and type the path here:  ")
        except ValueError:
            print("That's not a valid response. Please try again.")

# get user job listing and make parsed list

    job_listing = get_user_file(listing_text)

    user_list = []
    list_parser(key_list, job_listing, user_list)
    print("We have identified {} keywords from your job listing. ".format(len(user_list)))
    answer = input("Would you like to review the list? Yes/No   ")
    if answer.upper() == 'YES':
        print(user_list)
    else:
        break

#next ask user to review keyword list and add any others theyd like to check for

    while True:
        answer = input("Would you like to add any other words to the list? Yes/No/View   ")
        if answer.upper() == 'YES':
            word = input("What word or phrase would you like to add:  ")
            user_list.append(word)
        elif answer.upper() == 'VIEW':
            print(user_list)
        else:
            break  

# get user text file to compare to list  

    print('\n')
    print('*' *80)
    print('\n')      
    print("We can now compare the list you created to your cover letter or resume.\n")
    compare_text = input("Please save your document as a .txt file and type the path here:  ")              
    user_letter = get_user_file(compare_text)

# print results of comparisons (use class for multiple methods?)



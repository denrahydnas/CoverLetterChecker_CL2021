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
    answer = input("\nWould you like to check for keywords? Yes/No:   ")
    if answer.upper() == 'NO':
        break

# get user job listing and make parsed list

    listing_text = input("\nPlease save the job listing as a .txt file and type the path here:  ")
    job_listing = get_user_file(listing_text)

    user_list = []
    list_parser(key_list, job_listing, user_list)
    print("\nWe have identified {} keywords from your job listing. \n".format(len(user_list)))
    answer = input("\nWould you like to review the list? Yes/No/Quit   ")
    if answer.upper() == 'YES':
        print(user_list)
    if answer.upper() == 'QUIT':
        break


#next ask user to review keyword list and add any others theyd like to check for

    while True:
        answer = input("\nWould you like to add any other words to the list? Yes/No/View   ")
        if answer.upper() == 'YES':
            word = input("\nWhat word or phrase would you like to add:  ")
            user_list.append(word)
        elif answer.upper() == 'VIEW':
            print(user_list)
        else:
            break  

# get user text file to compare to list  

    print('\n')
    print('*' *80)
    print('\n')      
    print("We can now compare the list you created to your cover letter or resume.")
    compare_text = input("\nPlease save your document as a .txt file and type the path here:  ")              
    user_letter = get_user_file(compare_text)

# print results of comparisons (use class for multiple methods?)
    match_list = []
    list_parser(user_list, user_letter, match_list)
    print("\nWe have identified {} matching keywords.".format(len(match_list)))
    
    match_percentage = len(user_list)/len(match_list)
    print("\nYou have matched {}% of keywords identified from the job listing.".format(match_percentage))
    if match_percentage < 50:
            print("\nWe recommend adding more keywords in order to increase your match percentage.")
    
    unmatched = []
    unused_list(user_list, match_list, unmatched)

    answer = input("\nWould you like to review the lists? Yes/No   ")
    if answer.upper() == 'YES':
        print("\nYou used the following keywords: {}".format(match_list))
        print("\nYou did not use the following keywords: {}".format(unmatched))


# add a few more recommendations here - 
# split text by sentence, check how many begin with "I" using count()
# check sentence length and comma number, recommend cutting if over 12 words and has more than 1 comma
# if words are used more than 5 times in letter, show and recommend using synonyms


    answer = input("\nWould you like to compare other files? Yes/No/Quit  ")
    if answer.upper() == 'QUIT':
        print("\nOk, thank you - good luck on your job hunt!")
        break
    if answer.upper() == 'NO':
        print("\nOk, thank you - good luck on your job hunt!")
        break


from keyword_manip import *


#introduction

print("*"*80)
print("\n")
print("Welcome to my Job Application Keyword Checker.") 
print("Upload the listing for the job you are applying to and check it against our list of over 1,000 keywords.")
print("Then, compare your list to your cover letter or resume to make sure you've implememted as many keywords as possible.")
print("You can also check for a few more cover letter tips to help your application make it past the HR AI and increase the chances of the hiring staff seeing your application.  ")
print("\n")
print("*"*80)

# While loop for program

while True:
    answer = input("\nWould you like to check for keywords? Yes/No:   ")
    if answer.upper() == "NO":
        break

# get user job listing and make parsed list
    job_listing = try_file()

    user_list = []
    find_matches(master_list, job_listing, user_list)
    print("\nWe have identified {} keywords from your job listing.".format(len(user_list)))
    answer = input("\nWould you like to review the list? Yes/No/Quit   ")
    if answer.upper() == "YES":
        print(user_list)
    else:
        break


#next ask user to review keyword list and add any others theyd like to check for

    while True:
        answer = input("\nWould you like to add any other words to the list? Yes/No/View   ")
        if answer.upper() == "YES":
            word = input("\nWhat word or phrase would you like to add:  ")
            user_list.append(word)
        elif answer.upper() == "VIEW":
            print(user_list)
        else:
            break  

# get user text file to compare to list  

    print("\n")
    print("*" *80)
    print("\n")      
    print("We can now compare the list you created to your cover letter or resume.")          
    user_letter = try_file()

# print results of comparisons (use class for multiple methods?)
    match_list = []
    find_matches(user_list, user_letter, match_list)
    print("\nWe have identified {} matching keywords.".format(len(match_list)))
    
    match_percentage = round((len(match_list)/len(user_list)*100),2)
    print("\nYou have matched {}% of keywords identified from the job listing.".format(match_percentage))
    if match_percentage < 50:
            print("\nWe recommend adding more keywords in order to increase your match percentage.")
    
    unmatched = []
    unused_list(user_list, match_list, unmatched)

    answer = input("\nWould you like to review the lists? Yes/No   ")
    if answer.upper() == "YES":
        print("\nYou used the following keywords: {}".format(match_list))
        print("\nYou did not use the following keywords: {}".format(unmatched))
    
# parse cover letter for additional advice

    sentences = split_sentences(user_letter)
    start_i = i_start(sentences)
    percent_i =round((len(start_i)/len(sentences)*100), 2)
    too_long = long_sentence(sentences)

    print("\n")
    print("*"*80)
    print("\nWe also parsed your cover letter for a few other popular issues: ")
    print("\n{}, or {}% of the sentences in your letter begin with 'I'. We recommend rephrasing these sentences to be more about the applicable position".format(len(start_i), percent_i))
    answer = input("\nWould you like to review these sentences?  Yes/No/Quit ")
    if answer.upper() == "QUIT":
        break
    elif answer.upper() == "YES":
        for sentence in start_i:
            print("\n")
            print(sentence)

    print("\n{} of the sentences in your letter have over 150 characters. Could some of these sentences be shortened or divided for better readability? ".format(len(too_long)))
    answer = input("\nWould you like to review these sentences?  Yes/No/Quit ")
    if answer.upper() == "QUIT":
        break
    elif answer.upper() == "YES":
        for sentence in too_long:
            print("\n")
            print(sentence)

# parse words for overuse, recommend synonyms? 

#TBD

# leave program or start again 

    answer = input("\nWould you like to compare other files? Yes/No/Quit  ")
    if answer.upper() != "YES":
        print("\nOk, thank you - good luck on your job hunt!\n")
        print("*"*80)
        print("\n")
        break


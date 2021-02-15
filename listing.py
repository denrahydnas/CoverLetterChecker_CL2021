# Have User input Job Listing text - ok
# exclude errors
# remove punctuation - ok 
# use .lower to simplify - ok
# split words into job_listing list - ok
# get len of job_listing 
# combline duplicates
# get rid of unecessary words (the, of, or, to, etc) (loop against an Exclude list?)
# loop to check against keywords
# if match found, add word to found_keyword list
# print found_keyword list for User


import re

keyword_file = open("keywords.txt")
keyword_list = keyword_file.read()
keyword_file.close()


while True:
    answer = input("Would you like to check for keywords? Yes/No:   ")
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        try:
            listing_text = input("Please paste the text from the job listing here:     ")
            job_text = re.findall(r"[\w']+", listing_text.lower())
            print(job_text)
        except ValueError:
            print("That's not a valid response. Please try again.")
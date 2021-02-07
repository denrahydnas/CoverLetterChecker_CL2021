# Have User input Job Listing text - ok
# exclude errors
# remove punctuation - ok (https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters)
# use .lower to simplify - ok
# split words into job_listing list - ok
# get len of job_listing 
# combline duplicates
# get rid of unecessary words (the, of, or, to, etc) (loop against an Exclude list?)
# loop to check against keywords
# if match found, add word to found_keyword list
# print found_keyword list for User


import re

while True:
    answer = input("Would you like to check for keywords? Yes/No:   ")
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        try:
            job_text = input("Please paste the text from the job listing here:     ")
            parsed_text = re.findall(r"[\w']+", job_text.lower())
            print(parsed_text)
        except ValueError:
            print("That's not a valid response. Please try again.")
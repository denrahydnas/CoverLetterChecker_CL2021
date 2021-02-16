import re
from classes import KeyList

# Have User input Job Listing text - ok
# remove punctuation -use Regex for punct after words?
# disregard cases
# compare job listing to keyword list, create sub list (class)
# count duplicates
# print found_keyword list for User
# ask user to add missing keywords
# maybe - have user add .txt versions of job listing/cover letter/resume instead of copy/paste?
# compare found_keyword list to cover letter/ resume
# return matches


#introduction


print('*'*80)
print("Welcome to my Job Application Keyword Checker.") 
print("Upload the listing for the job you are applying to and check it against our list of over 1,000 keywords.")
print("Then, compare your list to your cover letter or resume to make sure you've implememted as many keywords as possible.")
print("You can also check for a few more cover letter tips to help your application make it past the HR computer system and make sure your application gets seen.  ")
print('*'*80)


job_title = input("What is the job title you are applying for?  ")
company_name = input("What is the name of the company?  ")
listing = input("Please paste the Job Listing here. Leave out the section about the Company:  ")
job_text = re.findall(r"\w'+", listing.lower())


kl = KeyList().create_keylist(job_text)
print(str(kl.k_list))
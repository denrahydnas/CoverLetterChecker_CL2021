# Have User input Job Listing text
# exclude errors
# remove punctuation
# use .lower to simplify
# split words into job_listing list 
# get len of job_listing 
# combline duplicates
# get rid of unecessary words (the, of, or, to, etc) (loop against an Exclude list?)
# loop to check against keywords
# if match found, add word to found_keyword list
# print found_keyword list for User


job_text = input("Please paste the text from the job listing here:     ")
job_listing = [job_text.split(" ")]
print(job_listing)

#not sure I need these bits after all:

while True:
    answer = input("Would you like to check for keywords? Yes/No:   ")
    if answer.upper() == 'NO':
        break
    if answer.upper() == 'YES':
        try:
            listing_text = input("Please paste the text from the job listing here:     ")
            job_text = re.findall(r"[\w']+", listing_text.lower())
            
        except ValueError:
            print("That's not a valid response. Please try again.")

add = input("would you like to add a Keyword to your search? Yes/No   ")

if add.upper() == "YES":
   KeyList.add(input("Please type the Keyword here:   "))
else:
    print("No worries, thanks!")

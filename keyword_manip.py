import re

#create master key list from txt file
master_key_list = []

keyword_file = open("keywords.txt", 'r')

for line in keyword_file.readlines():
    master_key_list.append([line])

# strip extra stuff out of the way - this removes interior space in 2 word answers- FIX ME
def key_clean(index):
    fixed = re.findall(r"[\w]+", str(master_key_list[index]))
    if len(fixed) <= 3:
        phrase = fixed[0]
    elif len(fixed) <= 4:
        phrase = fixed[0] + ' ' + fixed[1]
    elif len(fixed) <= 5:
        phrase = fixed[0] + ' ' + fixed[1]+ ' ' + fixed[2]
    else:
        phrase = (fixed[0] + ' ' + fixed[1] + ' ' + fixed[2]+ ' ' + fixed[3])
    return phrase

print(key_clean(456))

job_text = "I like to work with tablets and talent aquisition and play with products"

print(len(master_key_list))

for i in range(len(master_key_list)):
    if key_clean(i) in job_text:
        print(key_clean(i))
    



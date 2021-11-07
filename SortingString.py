"""
Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input
Sorting1234

Output
ginortS1324

"""

import re

sample_string = "".join(list(map(str,input())))
new_string = ""

patterns = [r"[a-z]",r"[A-Z]",r"[1,3,5,7,9]",r"[0,2,4,6,8]"]

for each in patterns:
    sub_li = re.findall(each,sample_string)
    sub_li.sort(reverse=False)
    new_string += "".join(sub_li)

print(new_string)

"""

Validate a Postal Code by following given condition

    -> The range of the postal code exists in 100000 and 999999.

    -> Cannot have same numvers at alternate positions.
        Eg : 232568, here 2 is repeated at alternate position


"""


# Driver Code

import re
postal_code = input()

#Validate the range of the postal code
#Find the length of the postal code has exactly six digits.
print(bool(re.match(r"\d{6}$",postal_code)))


#validate the numbers at alternate position

#Solution1: Using regex
print("Valid" if len(re.findall("(\d)(?=\d\1)", postal_code)) < 2 else "Invalid") ## URL : https://stackoverflow.com/questions/49325509/how-to-find-alternating-repetitive-digit-pair

#Solution2 : Using Lambda
def validate(a):
	ind = postal_code.index(a)
	ind_ = ind +2
	try :
		return True if postal_code[ind] == postal_code[ind_] else False
	except:
		return False

res = list(map(validate,postal_code))
print("valid" if res.count(True)<2 else "Invalid")

##Solution3 : Using Zip
res= [a for a,b in zip(postal_code,postal_code[2:]) if a==b]
print("valid" if len(res)<2 else "Invalid")

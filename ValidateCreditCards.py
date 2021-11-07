"""

Topic : Regex and Parsing 

Author : Phaneendhra

"""

import re

def check(string_iter):
    
    get_set = list(re.split(r"[-]",string_iter))
    
    if len(get_set)==4:
                    
        new_str= ""
                    
        for each in get_set:
            if len(each)==4:
                #print(each)
                new_str+=each
            else:
                return ""
    else:
        return ""
    
    return new_str

    
def validate_credit_card(string_iter):
    
    if (re.findall(r"[^-0-9]",string_iter) == []):
        if (re.findall(r"^[4,5,6]",string_iter) != []):
            if '-' in string_iter:
                 new = check(string_iter)
                 if new != "":
                     if len(new) == 16:
                         if (re.findall(r'((\w)\2{3,})', new) == []):
                             return "Valid"
                            
            else:
                if len(string_iter) == 16:
                         if (re.findall(r'((\w)\2{3,})', string_iter) == []):
                             return "Valid"
                
    return "Invalid"


if __name__ == "__main__":

    card_collections = [input() for each in range(int(input()))]
    print(*list(map(validate_credit_card,card_collections)),sep="\n")

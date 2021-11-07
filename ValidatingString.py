import re

def alphanumeric(s):
    if re.findall(r'[a-zA-Z0-9]',s)!=[]:
        return True
    return False
    
def alphabetical(s):
    if re.findall(r'[a-zA-Z]',s)!=[]:
        return True
    return False

def digits(s):
    if re.findall(r'[0-9]',s)!=[]:
        return True
    return False
    
def lowercase(s):
    if re.findall(r'[a-z]',s)!=[]:
        return True
    return False

def uppercase(s):
    if re.findall(r'[A-Z]',s)!=[]:
        return True
    return False
    
if __name__ == '__main__':
    s = input()
    list_=[ alphanumeric(s),
            alphabetical(s),
            digits(s),
            lowercase(s),
            uppercase(s)
          ]
    
    for each in list_:
        print(each)
    


def passwordCracker(passwords, loginAttempt,li_pass : dict()):
    # Write your code here
    """
    if loginAttempt == '':
        return li_pass
    """
    if passwords == []:
        return li_pass
    
    ress = loginAttempt.find(passwords[0])
    
    if ress !=-1:
        count_ = loginAttempt.count(passwords[0])
        #li_pass.append(passwords[0])
        if ress not in li_pass:
            li_pass[ress] = []
        li_pass[ress].append(passwords[0])
            
        loginAttempt = loginAttempt[:ress]+loginAttempt[ress+len(passwords[0]):]
        print(loginAttempt)
        #li_pass[ress] = passwords[0]
        
        if (count_==1):
            passwords = passwords[1:]    
        
        return passwordCracker(passwords, loginAttempt,li_pass)
    else:
        return "WRONG PASSWORD"

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        
        n = int(input().strip())

        passwords = input().rstrip().split()

        loginAttempt = input()

        result = passwordCracker(passwords, loginAttempt,{})

        print(result)

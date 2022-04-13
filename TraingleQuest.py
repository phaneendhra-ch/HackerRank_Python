"""
Sample Input
5

Sample Output
1
22
333
4444

"""

for i in range(1,int(input())): 
    print(10**i//9*i) # string literal is not used here
    
    #print(*list(*map(lambda i:[i]*i,[i])),sep="") #this case if string is accepted 

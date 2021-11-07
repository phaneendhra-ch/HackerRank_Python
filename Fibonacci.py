"""
Fibonacci using Map and Lambda

"""

cube = lambda x: x**3

def fibonacci(n):
    li = []
    first,second = 0,1                          # as febonacci starts from 0 and 1
    for _ in range(n):
        li.append(first)                        # append first to the list
        first,second = second,first + second    # update first with second and update second with sum of first + second  
    return li                                   # return fibonacci generated numbers till upto 5 occurences i.e.(0 1 1 2 3 )
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))        # here the list returned from fibonacci
                                                # map with lambda to generated cube of each digits
                                                

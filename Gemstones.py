"""
There is a collection of rocks where each rock has various minerals embeded in it. Each type of mineral is designated by a lowercase letter in the range . There may be multiple occurrences of a mineral in a rock. A mineral is called a gemstone if it occurs at least once in each of the rocks in the collection.

Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.

Example

3           arr[] size n = 3
abcdde      arr = ['abcdde', 'baccd', 'eeabg']
baccd
eeabg

Sample Output
2

Explanation
Only a and b occur in every rock

"""

def gemstones(arr):
    #Used Hash Maps    
    start = list(set(arr[0]))
    has_dict = dict(zip(start,[1]*len(start)))
    
    for each in range(1,len(arr)):
        for _ in list(set(arr[each])):
            if _ in has_dict:
                has_dict[_]+=1
    
    return len([k for k,v in has_dict.items() if v == len(arr)])
                
                    
    
        
    
if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    print(str(result) + '\n')



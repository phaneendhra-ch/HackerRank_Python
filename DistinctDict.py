"""
Print distince elements of dict by sorting value

"""

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    company_name = "aabbbccd"
    li = [each for each in company_name]
    dict_ = {}
    
    for each in li:
        if each in dict_:
            dict_[each]+=1
        else:
            dict_[each]=1
            
    dict_ = {key:value for key,value in sorted(dict_.items(), #<-- iterable
                                               key = lambda dict_: dict_[1],
                                               reverse=True)
            }
    
    for key,value in dict_.items():
        if value >1:
            print(key,value)

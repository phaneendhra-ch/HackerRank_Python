"""

This is not a part of HackerRank

Problem Statement :

    Remove duplicate lists from a list

    Input : list_ = [[1,2,3],[1,2,3],[4,5,6]]

    Output : list_ = [[1,2,3],[4,5,6]]

"""

a = [[1,2,3],[1,2,3],[4,5,6]]

a = list(map(lambda a:list(a),list(set(map(lambda a:tuple(a),a)))))

print(a)

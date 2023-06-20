def variable_num(a): 
    return (a[-1])

def tuples_sort(tuples):    
    return sorted(tuples, key= variable_num)

print(tuples_sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

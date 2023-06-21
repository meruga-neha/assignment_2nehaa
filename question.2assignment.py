tuple_number = [(2, 5), (1, 2), (4, 4), (2, 3),(2, 1)]
print("list of orginal tuples :" ,tuple_number)
def sort(tuple_number):  
    tuple_number.sort(key = lambda a: a[1]) 
    return tuple_number 

print("list of tuples sorted:" ,sort(tuple_number))
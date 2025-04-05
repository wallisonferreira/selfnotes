list_of_items = [15, 20, 29, 35, 36, 37, 40, 46, 47, 48]

item = 47

def binary_search(item, list_of_items):
    size = len(list_of_items)
    middle_index = (size // 2)
    print((middle_index, size))
    print(list_of_items)
    if item == list_of_items[middle_index]:
        print("Achamos o {}".format(item))
    elif item > list_of_items[middle_index]:
        binary_search(item, list_of_items[middle_index+1:]) 
    elif item < list_of_items[middle_index]:
        binary_search(item, list_of_items[:middle_index])
    else:
        print("Erro")
        
binary_search(47, list_of_items)

# This is (o)logn complexity because for each statement
# we decrease the number of steps by halves

# It's a series of iterations that divide a sorted list
# in half to drill down to a specific element.
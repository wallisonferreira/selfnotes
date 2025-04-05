def find_min_linear(list_numbers):
    minimum = list_numbers[0]
    
    for i in list_numbers:
        if minimum > i:
            minimum = i
            
    return minimum
            
print(find_min_linear([12, 9, 4, 2, 3, 6]))
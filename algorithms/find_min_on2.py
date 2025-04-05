import random
import time

def find_min(list_numbers):
    overall_min = list_numbers[0]
    iterations = 0
    
    for i in list_numbers:
        is_smallest = True
        for j in list_numbers:
            if i == j:
                continue
            iterations += 1
            
            if i > j:
                is_smallest = False
                
        if is_smallest:
            overall_min = i
                
    print("Minimum is: " + str(overall_min))
    print("number of iterations: " + str(iterations))
    

find_min([2,4,7,8,25])
    
for list_size in range(1000, 10001, 1000):
    a_list = [random.randrange(100000) for x in range(list_size)]
    start = time.time()
    find_min(a_list)
    end = time.time()
    print("size: %d | time: %s" % (start, end))
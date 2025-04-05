# Given a non-empty list of integers, every element 
# appears twice except for one. Find that single one.

def find_single_one(arr):
    count_words = {}
    for i in arr:
        if i in count_words:
            count_words[i] += 1
        else:
            count_words[i] = 1
            
    for key, value in count_words.items():
        if value == 1:
            return key

arr = [5,5,6,6,8,7,7,4,4]

print(find_single_one(arr))   
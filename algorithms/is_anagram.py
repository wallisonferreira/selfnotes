word_1 = "cinema"
word_2 = "iceman"

word_1 = word_1.lower()
word_2 = word_2.lower()

if sorted(word_1) == sorted(word_2):
    print("is an anagram!")
else:
    print("is not a anagram!")
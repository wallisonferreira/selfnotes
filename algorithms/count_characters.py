def count_words(text):
    words_dict = {}
    for c in text:
        if c in words_dict:
            words_dict[c] += 1
        else:
            words_dict[c] = 1
    print(words_dict)

text = "antidescontanticionalissimamente"
count_words(text)
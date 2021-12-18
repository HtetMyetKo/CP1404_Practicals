letters_set = {}
string = input("Text: ")
words = string.split()
for word in words:

    count = letters_set.get(word, 0)
    letters_set[word] = count + 1

words = list(letters_set.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, letters_set[word]))
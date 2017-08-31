words = {}
words_to_count = input("Enter a string: ")

for word in words_to_count.split():
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

MAX_LENGTH = max(len(word) for word in words.keys())

my_list = ["{:{}} : {}".format(key, MAX_LENGTH, value) for key, value in words.items()]
my_list.sort()
for pair in my_list:
    print(pair)

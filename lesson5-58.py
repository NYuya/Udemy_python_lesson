print('Lesson 5-58')
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
    for word in words:
        print(func(word))


# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()


# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

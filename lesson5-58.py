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


print('Lesson 5-59')
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print("#############")


def counter(num=10):
    for _ in range(num):
        yield 'run'


def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'


# for g in greeting():
#     print(g)

g = greeting()
c = counter()
print(next(g))
print("@@@@")
print(next(c))

print(next(g))
print("@@@@")
print(next(c))
print(next(c))

print(next(g))


print('Lesson 5-60')
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)
print(r)

r = [i for i in t if i % 2 == 0]
print(r)


r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

# リスト内包表記は無駄に使ってはいけない
r = [i * j for i in t for j in t2]
print(r)

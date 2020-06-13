print('Lesson 5-48')


def say_something():
    print('hi')


say_something()


def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"


result = what_is_this('red')
# result = what_is_this('green')
# result = what_is_this('yellow')
print(result)


print('Lesson 5-50')


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func(100)
print(r)

r = test_func(100)
print(r)

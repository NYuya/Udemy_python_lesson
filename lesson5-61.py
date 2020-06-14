print('Lesson 5-61')
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)


print('Lesson 5-62')
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)


print('Lesson 5-63')


def g():
    for i in range(10):
        yield i


g = g()

g = (i for i in range(10) if i % 2 == 0)
print(type(g))
print(g)
for x in g:
    print(x)


print('Lesson 5-63')
animal = 'cat'


def f():
    # print(animal)
    animal = 'dog'
    print('after', animal)


f()
print('globa:', animal)


"""
Test ###############
"""
animal = 'cat'


def f():
    """Test func doc"""
    # print(f.__name__)
    # print(f.__doc__)


f()
print('global:', globals())

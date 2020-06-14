print('Lesson 5-53')


def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree='beef', drink='coffee')


d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)


def menu(food, *args, **kwargs):  # 「＊」の順番、小さい順に並べる
    print(food)
    print(args)
    print(kwargs)


menu('banana', 'apple', 'orange', entree='beef', drink='coffee')


print('Lesson 5-55')


def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(a, b)
    print(r1 + r2)


outer(1, 2)


print('Lesson 5-56')


def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area


ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))


print('Lesson 5-57')


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


def add_num(a, b):
    return a + b


f = print_info(add_num)
r = f(10, 20)
print(r)


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper


@print_info
def add_num(a, b):
    return a + b


r = f(10, 20)
print(r)


def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper


def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# @print_infoと@print_moreの順序が大切
@print_info
@print_more
def add_num(a, b):
    return a + b


r = f(10, 20)
print(r)

class UppercaseError(Exception):
    pass


def checj():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)


try:
    check()
except UppercaseError as exc:
    print('Tis is my fault. Go next')

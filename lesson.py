# 4-18
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print("exist")

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)


s = 'My name is Mike'

# 空白がある事でスプリットで分けてくれる
to_split = s.split(' ')
print(to_split)

# 空白で繋いでくれる
x = ' '.join(to_split)
print(x)

# メソッド一覧表示
# print(help(list))

# 5-33
x = 11

if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')


a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')


print('Lesson 5-39')
# count = 0

# while count < 5:
#     print(count)
#     count += 1

count = 0

while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1


print('Lesson 5-40')
count = 0

while count < 5:
    if count == 1:
        break
    print(count)
    count += 1
else:
    print('done')


print('Lesson 5-41')
while True:
    word = input('Enter:')
    num = int(word)
    if num == 100:
        break
    print('next')


print('Lesson 5-42')
some_list = [1, 2, 3, 4, 5]

i = 0

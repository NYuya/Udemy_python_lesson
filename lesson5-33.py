
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

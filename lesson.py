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
to_split = s.split(' ')  # 空白がある事でスプリットで分けてくれる
print(to_split)

x = ' '.join(to_split)  # 空白で繋いでくれる
print(x)

print(help(list))  # メソッド一覧表示

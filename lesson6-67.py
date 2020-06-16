from collections import defaultdict
import builtins
print('Lesson 6-67')

print('Lesson 6-73 組み込み関数')
print(globals())
builtins.print()

ranking = {
    "A": 100,
    "B": 85,
    "C": 95
}

print(sorted(ranking, key=ranking.get, reverse=True))


print('Lesson 6-74 標準ライブラリ')
s = "fdjsafiewafjdsaeiwfdafke"

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)


d = defaultdict(int)

for c in s:
    d[c] += 1
    print(d)

print(d['f'])

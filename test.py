import pyperclip as clipboard

from map import island
print(island)

new_map = []
for x in island:
    buffer = []
    for y in x:
        buffer.append(y)
    for _ in range(55):
        buffer.append(y)
    new_map.append(buffer)
for _ in range(25):
    new_map.append(buffer)

print(len(island), len(island[0]))
print(len(new_map), len(new_map[0]))
with open(f'map.py', mode='w') as f:
    f.write('island = ' + str(new_map))
print('Writed.')
=======
a = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]

k = 2, 2
c = 1, 1
res = []
n = 0
for i in a:
    if n < k[0]:
        m = 0
        r = []
        for j in i:

            if m < k[1]:
                r.append(j)
                m += 1
        res.append(r)
        n += 1
print(res)

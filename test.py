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

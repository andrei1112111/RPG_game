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

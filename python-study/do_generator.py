def triangles(n):
    if n>=1:
        yield [1]
    if n>=2:
        last = [1,1]
        yield last
    j = 3
    while j<=n:
        res = [1]
        i = 0
        for i in range(len(last)-1):
            x = last[i]+last[i+1]
            res.append(x)
        res.append(1)
        last = res
        yield res
        j = j+1
    return 'done'


g = triangles(12)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
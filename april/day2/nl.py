x = [int(i) for i in input().split()]
k = x[-1]
x.remove(x[-1])
x.sort()
print(' '.join(list(map(str,x[:k]))))
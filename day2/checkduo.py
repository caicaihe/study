#两个数组中相同的元素
a = [1,2,3,4,52]
b = [2,3,21,34,5]
aset = set(a)
bs = set(b)
m = aset & bs
n = aset | bs
n.sort()
print(m,n)
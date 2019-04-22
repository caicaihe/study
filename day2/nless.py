#list中的前n个最小的数
def nless(N):
    #N.sort() 
    N = sorted(N)
    return N



if __name__ == '__main__':
    n = 3
    N = [1,3,4,5,2,45,5]
    m = nless(N)
    print(N, m[0:n])
    

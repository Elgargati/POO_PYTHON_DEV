def occurence(L):
    # D={}
    # for i in L:
    #     D[i]=L.count(i)
    # return D
    D={}
    for i in L:
        D[i]=L.count(i)
    return D


L=[1,2,1,2,4,1,3,5,1,1,1]
print(occurence(L))
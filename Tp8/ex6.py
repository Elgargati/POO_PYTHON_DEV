def Longureur(T):
    # D={}
    # L=T.split()
    # for i in L:
    #     D[i]=len(i)
    # return D
    D={}
    L=T.split()
    for i in L:
        D[i]=len(i)        
    return D


T=input("donner un text ")
print(Longureur(T))




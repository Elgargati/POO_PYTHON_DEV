def Parite(L):
    # D={}
    # for i in L:
    #     if i%2==0:
    #         D[i]="paire"
    #     else:
    #         D[i]="impaire"
    # return D
    D={}
    for i in L:
        if i%2==0:
            D[i]="paire"
        else:
            D[i]="impaire"
    return D

L=[1,2,1,44,3,4,5,3,2,56,3,4553,245,323,34]
print(Parite(L))
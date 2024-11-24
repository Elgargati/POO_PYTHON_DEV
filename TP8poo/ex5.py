def Parite(L):
    d={}
    for i in L :
        if i%2==0 :
           d[i]="paire"
        else :
            d[i]="impaire"

    return d

L=[1,2,3,4,5,6,7,8,9]
print(Parite(L))
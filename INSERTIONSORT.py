#INSERTION SORT

a=[8,4,9,2,7,-10000000]
for i in range(1,len(a)):
    while(i>0):
        if(a[i]<a[i-1]):
            a[i],a[i-1]=a[i-1],a[i]
            i-=1
        else:
            break

print(a)
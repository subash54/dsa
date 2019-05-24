#SELECTION SORT
a=[9,4,7,8,2,5]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            a[j],a[i]=a[i],a[j]
print("The sorted array\n",a)



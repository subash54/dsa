a=[25,4,3,9,7]
for i in range(1, len(a)):
    t=a[i]
    j=i-1
    while(j>=0):
        if a[j]>t:
            a[j],a[j+1]=a[j+1],a[j]
            j=j-1
        else:
            break
print(a)
def quick(arr,l,h):
    if(l<h):
        p=partition(arr,l,h)
        quick(arr,l,p-1)
        quick(arr,p+1,h)
def partition(arr,l,h):
    i=l-1
    p=arr[h]
    for j in range(l,h):
        if arr[j]<=p:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1
a=[1,5,2,7,3,8]
quick(a,0,len(a)-1)
print(a)

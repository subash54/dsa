def merge(l,m,r,ar):
 a=[]
 b=[]
 c=[]
 for i in range(l,m):
      a.append(ar[i])
 for j in range(m,r+1):
        b.append(ar[j])
 i=0
 k=l
 j=0
 while i<len(a) and j<len(b):
        if(a[i]<b[j]):
            ar[k]=a[i]
            i+=1
            k=k+1

        else:
            ar[k]=b[j]
            j+=1
            k=k+1

 while(i<len(a)):
        ar[k]=a[i]
        i+=1
        k+=1
 while(j<len(b)):
        ar[k]=b[j]
        j+=1
        k+=1



def mergesort(l,r,ar):
   if(l<r):
    m=(l+r)//2

    mergesort(l,m,ar)
    mergesort(m+1,r,ar)

    merge(l,m,r,ar)


ar = [9, 1, 5, 6, 2, 3]
w=mergesort(0,5,ar)
print(ar)
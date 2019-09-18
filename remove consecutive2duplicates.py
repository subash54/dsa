t=int(input())
k=[]
for j in range(t):
    a = input()
    k.append((a))

for a in k:
 stack = []
 for i in range(len(a)):
   if (i == 0):
     stack.append(a[i])
   elif len(stack)==0:
     stack.append(a[i])

   elif a[i] == stack[-1]:
        stack.pop()
   else:
        stack.append(a[i])
 d=""
 if(len(stack)==0):
     print("$")
 else:
     print(d.join(stack))


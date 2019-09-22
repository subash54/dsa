t=int(input())
as1=[]
for i in range(t):
 a=list(input())
 as1.append(a)
for a in as1:
    stack=[]
    i=0
    b=""
    k=""
    def priority(a):
        if(a=='+' or a== '-'):
            return 1
        elif(a=='/' or a=='*'):
            return 2
        elif(a=='^'):
            return 3
    while(i!=len(a)):
        if(a[i]=='^'):
            stack.append(a[i])
            i=i+1
            continue
        if(a[i]>='A' and a[i]<='z') or (a[i]>='a' and a[i]<='z'):
            b=b+a[i]
            i=i+1
           # print(b)
        else:

            if(len(stack)==0):
                stack.append(a[i])
                i+=1
                #print(stack)

            else:
                if (a[i] == '(' ):
                    stack.append(a[i])
                    i+=1
                elif (a[i] == ')'):
                    while (stack[-1] != '('):
                        b=b+stack.pop()
                    stack.pop()
                    i=i+1


                elif(stack[-1]=='('):
                    if (a[i]>='a'and a[i]<='z') or(a[i]>='A' and a[i]<='Z'):
                      b=b+a[i]
                      i=i+1
                    else:
                        stack.append(a[i])
                 #       print("                               ",stack)
                        i=i+1
                elif(priority(a[i])>priority(stack[-1])):
                    stack.append(a[i])
                    i = i + 1
                else:
                    b=b+stack.pop()
                #print(stack,b)


    while(len(stack)!=0):
       b=b+stack.pop()
    print(b)
temp=int(input())
ar=[]
for i in range(temp):
    string =input()
    ar.append(string)
for string in ar:
 stack=[]
 for i in string:
        if(i=='*') or(i=='-')or(i=='+')or(i=='/'):
            x1=int(stack.pop())
            x2=int(stack.pop())
            d=0
            if(i=='*'):
                d=x2*x1
            elif(i=='/'):
                d=x2//x1
            elif(i=='-'):
                d=x2-x1
            elif(i=='+'):
                d=x2+x1
            stack.append(d)
        else:
               stack.append(i)
 print(stack.pop())



def priority(x):
    if (x == '{'):
        return '}'
    elif (x == '['):
        return ']'

    elif (x == '('):
        return ')'


t = int(input())
res=[]
for k in range(t):
    a = input()
    i = 0
    stack = []
    d=0
    for i in a:
        if (i == '{' or i == '[' or i == '('):
            stack.append(i)
        elif (i == ')' or i == ']' or i=='}'):
            if (len(stack) == 0):
                d=-1
                break
            d = priority(stack[-1])
            if (d == i):
                stack.pop()
            else:
                d=-1
                break
    if (len(stack) == 0) and d!=-1:
        res.append("balanced")
    else:
        res.append("not balanced")
for j in res:
    print(j)
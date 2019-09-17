def _push(a, n):
    s=[]
    s.append(a[0])
    for i in range(1,n):
        if(s[-1]>a[i]):
            s.append(a[i])
        else:
            s.append(s[-1])
    return s

def _getMinAtPop(stack):
    # code here
    d = len(stack)
    for i in range(d):
        print(min(stack), end=" ")
        stack.pop()

n = int(input())
a = list(map(int, input().strip().split()))
stack1 =_push(a, n)  # our stack to be used
_getMinAtPop(stack1)  # print elements of stack as required


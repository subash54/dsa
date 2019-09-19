def deleteMid(s, sizeOfStack, current):
    ##Your code here
    s1 = []

    mid = sizeOfStack // 2
    if (sizeOfStack % 2 != 0):
        mid = mid + 1
    while (sizeOfStack != mid):
        s1.append(s.pop())
        sizeOfStack -= 1
    s.pop()
    s1.reverse()
    s = s + s1
    return s

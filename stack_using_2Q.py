 queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    queue_2.append(x)
    while(len(queue_1)!=0):
        d=queue_1.pop()
        queue_2.insert(0,d)
    while(len(queue_2)!=0):
        queue_1.insert(0,queue_2.pop())
    
    
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    if(len(queue_1)==0):
        return -1
    return queue_1.pop()
    
    

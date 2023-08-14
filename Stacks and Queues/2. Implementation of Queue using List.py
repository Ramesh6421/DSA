n=[5]
Queue=[-1]*n[0]
count=[0]
front=[0]
rear=[0]

def push(x):
    if count[0]==n[0]:
        return -1
    Queue[rear[0]%n[0]]=x
    rear[0]+=1
    count[0]+=1
    print(Queue)
    return

def pop():
    if count==0:
        return -1
    Queue[front[0]%n[0]]=-1
    front[0]+=1
    count[0]-=1
    print(Queue)
    return

def top():
    if count[0]==0:
        return -1
    return Queue[front[0]]


push(1)
push(2)
pop()
print(top())
push(3)
push(4)

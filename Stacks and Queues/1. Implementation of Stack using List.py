
stack=[]

def push(x):
    stack.append(x)

def pop():
    return stack.pop()

def top():
    return stack[-1]

def size():
    return len(stack)

def isEmpty():
    return False if stack else True 

push(1)
push(2)
print(pop())
push(3)
print(top())
print(size())
print(isEmpty())

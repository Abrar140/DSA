top = -1
arr = [0] * 5  # Creates a list of size 5 filled with 0

def push(num, arr, top):
    if top == len(arr) - 1:
        print("Stack is full")
        return top  # Return the unchanged top
    else:
        top += 1
        arr[top] = num
        print(f"Pushed {num} to stack at position {top}")
        return top  # Return the updated top
def pop(arr, top):
    if top==-1:
        print("Staack is empty")
        return top
    else:
        top=top-1
        return top

def printStack(arr, top):
    for x in range(top+1):
        print(x)

def returnTop(arr, top):
    return arr[top]
def isEmpty(top):
    if top==-1:
        return True
    else:
        return False
def isFull(arr, top):
    if top == len(arr) - 1:
        return True  
    else:
        return False
def SizeofStack(top):
    return top+1

def ClearStack():
    return -1

# Update the `top` value after each push
top = push(1, arr, top)
top = push(2, arr, top)
top = push(3, arr, top)
top = push(4, arr, top)
top = push(5, arr, top)  
top= pop(arr,top)
top = push(6, arr, top)  
printStack(arr,top)  # Final stack
print("element on top is ",returnTop(arr,top))

print("isFull",isFull(arr, top) )
print("Size of Stack",SizeofStack( top) )
top=ClearStack()
print("isEmpty", isEmpty(top))






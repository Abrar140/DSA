def access(arr, index, size):
    if 0 <= index < size:
        return arr[index]
    return "Index out of bounds"

def update(arr, index, value, size):
    if 0 <= index < size:
        arr[index] = value
        return arr
    return "Index out of bounds"

def traversal(arr, size):
    for i in range(size):
        print(arr[i])
    print()

def insertion(arr, index, value, size):
    if size >= len(arr):
        return "Array is full"
    if index < 0 or index > size:
        return "Index out of bounds"

    i = size
    while i > index:
        arr[i] = arr[i - 1]
        i -= 1

    arr[index] = value
    return arr

def deletion(arr, index, size):
    if index < 0 or index >= size:
        return "Index out of bounds", size

    i = index
    while i < size - 1:
        arr[i] = arr[i + 1]
        i += 1
    arr[size - 1] = 0  # optional: clear last element
    size -= 1
    return arr, size

def searchbyindex(arr, index, size):
    return access(arr, index, size)

def searchbyvalue(arr, key, size):
    for i in range(size):
        if arr[i] == key:
            return f"Found at index {i}"
    return "Not found"


# ----------- Usage -----------

arr = [0] * 10  # fixed size array
size = 0        # logical size (number of valid elements)

# Insert 5 values
for val in [10, 20, 30, 40, 50]:
    insertion(arr, size, val, size)
    size += 1

print("Initial array:")
traversal(arr, size)

print("Access index 2:", access(arr, 2, size))

update(arr, 2, 999, size)
print("After update index 2 to 999:")
traversal(arr, size)

print("Insert 555 at index 3:")
insertion(arr, 3, 555, size)
size += 1
traversal(arr, size)

print("Delete element at index 4:")
arr, size = deletion(arr, 4, size)
traversal(arr, size)

print("Search value 555:", searchbyvalue(arr, 555, size))
print("Search value 123:", searchbyvalue(arr, 123, size))

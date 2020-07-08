def binary_search(arr, low, high, x):
    
    if high >= low:

        mid = (high + low) // 2

        
        if arr[mid] == x:
            return mid

            
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

            
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


print("Enter The Size Of The Array : ", end="\n")
size = int(input())
arr = []
print("Enter ", size, "Elements  In Ascending Order: ")
for i in range(size):
    x = int(input())
    arr.append(x)
print("Enter The Element To Do Binary Search : ", end="\n")
ele = int(input())


result = binary_search(arr, 0, size - 1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

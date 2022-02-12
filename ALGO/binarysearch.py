def search(arr,key):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right) //2

        if arr[mid] == key:
            return mid
        if arr[mid] < key:
            left +=1 # or left = mid + 1
        else:
             
            right -=1 # right = mid -1


    return 0


arr = [2, 3, 4, 10, 40]
key= 10
# Function call
result = search(arr,key)
if(result == 0):
    print("Element is not present in array")
else:
    print("Element is present at index", result)



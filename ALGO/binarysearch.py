def search(arr,key):
    left = 0
    right = len(arr)-1
    for i in range(len(arr)):
        while left <= right:
            mid = (left + right) //2

            if arr[mid] == key:
                return mid
            if arr[mid] < key:
                left +=1
            if arr[mid] > key:
                right -=1


        return 0


arr = [2, 3, 4, 10, 40]
key= 10
n = len(arr)
# Function call
result = search(arr,key)

if(result == 0):
    print("Element is not present in array")
else:
    print("Element is present at index", result)



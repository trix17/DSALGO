def search(n,key):
    for i in range(len(n)):
        if n[i] == key:
            return(i)



    return 0




arr = [2, 3, 4, 10, 40]
key= 0
n = len(arr)
# Function call
result = search(arr,key)

if(result == 0):
    print("Element is not present in array")
else:
    print("Element is present at index", result)
    
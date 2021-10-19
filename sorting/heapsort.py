def heapify(arr,n,i):

    largest = i
    l = 2 * i +1
    r = 2* i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]



        heapify(arr,n,largest)

def heapsort(arr):
    n = len(arr)


    #Build  a max heap
    for i in range(n//2why ):
        heapify(arr,n,i)
    

    #Extract on by one
    for i in range(n-1, 0, -1):
        arr[i],arr[0] = arr[0],arr[i]
        heapify(arr,i,0)



arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])

def partition(arr,start,end):
    

    p_index = start
    pivot = arr[end]
    


    for i in range(start,end):
        if arr[i]<= pivot:
            arr[i],arr[p_index] = arr[p_index], arr[i]
            p_index +=1

    arr[p_index],arr[end] = arr[end],arr[p_index]
    return p_index

def quicksort(arr,start,end):
    if (start < end):
        p = partition(arr,start,end)
        
        quicksort(arr,start,p-1)
        quicksort(arr,p+1, end)




arr = [ 10, 7, 8, 9, 1, 5 ]
quicksort(arr,0,len(arr)-1) 
print(f'Sorted array: {arr}')
      

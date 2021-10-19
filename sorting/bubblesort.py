def bubblesort(n):
    for i in range (len(n)):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]








n = [-2,45,0,11,-9]
bubblesort(n)
print("The sorted array is:")
for i in range(len(n)):
    
    print(n[i])




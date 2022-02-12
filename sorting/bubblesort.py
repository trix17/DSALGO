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


"""
I have alway had problem with nested loop 
basic logic so I can remmeber, next time I revisit Bubblesort

the outter loop keeps track of how many time we will run this program , 
the inner loop is all the numbers part of the array that will be printed
n amount of times  (outter loop ). 
before executing the algorithm 
if we just print n[j] of the outter loop 
the result will be [-2,45,0,11,-9], [-2,45,0,11,-9], [-2,45,0,11,-9], [-2,45,0,11,-9], [-2,45,0,11,-9]
until we start moving numbers in ascending order. 



"""

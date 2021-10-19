def insertion(n):
    for i in range(1,len(n)):
        key = n[i]
        j = i -1 

        while j >= 0 and n[j] > key:
            n[j +1] = n[j]
            j = j-1






        n[j+1] = key

n = [12, 11, 13, 5, 6]
insertion(n)
for i in range(len(n)):
    print ("% d" % n[i])



 

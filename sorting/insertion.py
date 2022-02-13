"""def insertion(n):
    for i in range(1,len(n)):
        key = n[i]
        j = i -1 

        while j >= 0 and n[j] > key:
            n[j +1] = n[j]
            j = j-1






        n[j+1] = key"""

def insertion(n):
    for i in range(1,len(n)):
        value = n[i]
        while i > 0 and n[i-1] > value:
            n[i] = n[i-1] #[12, 11, 13, 5, 6] become [12, 12, 13, 5, 6]
            i = i- 1 # will be 0 therefore breaks the loop
        n[i] = value 
    return value



n = [12, 11, 13, 5, 6]
insertion(n)
for i in range(len(n)):
    print ("% d" % n[i])



 

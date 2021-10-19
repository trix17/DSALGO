def merge(n):
    if len(n) > 1:
        mid = len(n) //2

        l = n[:mid]
        r = n[mid:]

        merge(l)
        merge(r)

        i = j = k = 0

        while i < len(l) and j < len(r):

            if l[i] < r[j]:

                n[k] =l[i]
                i +=1
                k+=1
            else:

                n[k] = r[j]
                j+=1
                k+=1
        
        while i < len(l):
            n[k] =l[i]
            i +=1
            k +=1

        while j < len(r):
            n[k] =r[j]
            j +=1
            k +=1 



n  = [12, 11, 13, 5, 6]
merge(n)
for i in range(len(n)):
    print ("% d"% n[i])
 

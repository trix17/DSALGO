def counting(n,max_value):

    m = max_value + 1
    count = [0]* m 
    for a in n:
        count[a] +=1

    i = 0 
    for a in range(m):
        for c in range(count[a]):
            n[i] = a
            i +=1

    return n



print(counting( [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1], 7 ))

def maxcrossing(n,l,m,h):

    left_sum = -10000
    sm = 0 

    for i in range (m,l-1,-1):
        sm = sm + n[i]
        if (sm > left_sum):
            left_sum = sm 
    # ---------------------------------#        
    right_sum = -10000
    sm = 0 

    for i in range (m+1,h+1):
        sm = sm + n[i]
        if (sm > right_sum):
            right_sum = sm 


    return max(left_sum + right_sum , left_sum, right_sum)

def maxsub(n,l,h):
    if (l == h):
        return n[l]

    m = (l+h) // 2 

    return max(maxsub(n,l,m),
            maxsub(n,m+1,h),
            maxcrossing(n,l,m,h))



n = [2, 3, 4, 5, 7]
m = len(n)
 
max_sum = maxsub(n, 0, m-1)
print("Maximum contiguous sum is " , max_sum)






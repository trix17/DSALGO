import sys
def maxsubarray(n):
    max_so_far =- sys.maxint-1
    max_end_here = 0


    for i in range(len(n)):
        max_end_here = max_end_here + n[i]

        if (max_so_far < max_end_here):
            max_so_far = max_end_here
        if max_end_here < 0 :
            max_end_here = 0


    return max_so_far





n = [-2,-3,4,-1,-2,1,5,-3]
print("Maximum contiguous sum is",maxsubarray(n))


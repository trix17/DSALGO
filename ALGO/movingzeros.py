def move_z(list):
    z_index = 0
    for i, n in enumerate(list):
        if n != 0:
            list [z_index] = n 
            if z_index != i:
                list[i] = 0

            z_index +=1


    return list

list = [7,6,0,1,0,9]
move_z(list)
print(list)            
"""
algo expalnation :
first loop : z_index increment to 1
second loop same , since it is not equal to zero, increment index 2
third loop no increment since n = 0 at index 2 , 
fourth loop list[z_index] will become : 7,6,1,1...
 and since index 2 is not equal to 3 list[i] will be 0 [7,6,1,0] and so on...

"""
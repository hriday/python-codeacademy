# You are given an n x n 2D matrix that represents an image. 
# Rotate the image by 90 degrees (clockwise).

#Example

#For

#a = [[1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

#the output should be

#rotateImage(a) =
#    [[7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]]

# Hriday: 2020/07/05

# Initialize a new array with the same size 
# as a. Make user you don't b = a. Use deepcopy
# or what's done below. After that, the logic is
# b[i][j] = a[(len-1)-i][i]. Just iterate through
# the array and return b.


def rotateImage(a):
    b = [row[:] for row in a]
    alen = (len(a)-1)
    print (alen)
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            b[i][j] = a[alen-j][i]
    return (b)

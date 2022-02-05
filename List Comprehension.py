# Let's learn about list comprehensions! You are given three integers  and  representing the
# dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by (i,j,k)
# on a 3D grid where the sum of i+j+k is not equal to n. Here, 0<=i<=x;0<=j<=y;0<=k<=z.
# Please use list comprehensions rather than multiple loops, as a learning exercise.

# Sample Input 0
#x = 1
#y = 1
#z = 1
#n = 2

#Sample Output 0
#[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
# Note: if the sum of each list inside the parent list equal to n=2, remove it from the parent list

# Answer 1:

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arrays = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    for l in arrays[:]:
        if sum(l) == n:
            arrays.remove(l)
    
    print(arrays)
    
 # Answer 2:
 
 if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arrays = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    new_arrays = [m for m in arrays if sum(m) !=n]
    
    print(new_arrays)

 

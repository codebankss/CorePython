i = int(input("Enter number of rows"))
j = int(input("Enter number of columns"))

A = [ [ [ ] for a in range(i)] for a in range(j)]

for a in range(0, i):
    for b in range(0, j):
        number = int(input("Enter the elements of matrix"))
        A[a][b] = number
        print(A)
 

for matrix in A: 
    print(matrix) 
print("\n") 
t_A = zip(*A) 
for row in t_A: 
    print (matrix) 

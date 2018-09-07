#transpose of nested list

i = int(input("Enter number of rows"))
j = int(input("Enter number of columns"))

A = [ [ [ ] for a in range(i)] for a in range(j)]

for a in range(0, i):
    for b in range(0, j):
        number = int(input("Enter the elements of matrix"))
        A[a][b] = number
        print(A)
 
for matrix in A : 
    print(matrix) 
result = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
print("\n")

for matrix in result: 
    print(matrix) 

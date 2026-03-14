rows = 3
column = 3
Matrix = []

for i in range(rows):
    rowArray = []
    for j in range(column):
        rowArray.append(j) 
    Matrix.append(rowArray)

print(Matrix)

# traversing the array
for i in range(rows):
    for j in range(column):
        print(Matrix[i][j],end=" ")
    print()

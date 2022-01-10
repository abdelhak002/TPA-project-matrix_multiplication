import time

X = []  # inisialize the first matrix which is a simple array
x_rows = int(input("enter the rows of the matrix X: ")) # number of rows of first matrix
x_columns = int(input("enter the columns of the matrix X: ")) # number of columns of second matrix
print("Enter the items of Matrix X[i][j]:")
# filling the first matrix elements
for i in range(x_rows):
    Xrows = [] # array will store the elements of row
    for j in range(x_columns):
        rows = int(input('item[%d][%d]: ' % (i, j))) # filling every single element of the row
        Xrows.append(rows) # adding the element to the end of the row (which is a simple array)
    X.append(Xrows) # adding the rows(arrays) to the end of the X[] array
print("the first Matrix X: ", X) # printing the matrix, so basicllay the matrix here is an array containing arrays
# for example 
# Matrix_x = [[1,2,3],[4,5,6],[7,8,9]]

# same approache done with the second matrix
Y = []
y_rows = x_columns # the rule of matrix multiplication 
y_columns = int(input("enter the columns of the matrix Y: "))
print("Enter the items of Matrix Y[i][j]: ")
for i in range(y_rows):
    Yrows = []
    for j in range(y_columns):
        rows = int(input('item[%d][%d]: ' % (i, j)))
        Yrows.append(rows)
    Y.append(Yrows)
print("the Second Matrix Y: ", Y)


# empty array for resulatant matrix
resultant = []
 
# set the size of the resultant matrix to the appropriate values
for i in range(x_rows):
    row = []
    for j in range(y_columns):
        row.append(0)
 
    resultant.append(row)
 
print("Matrix Multiplication: ")

start = time.time()
# perform matrix multiplication
# using nested for loops
for i in range(x_rows):
    for j in range(y_columns):
        for k in range(x_columns) :
            resultant[i][j] += X[i][k] * Y[k][j]
 
# matrix printing row wise            
for row in resultant:
    print(row)

end = time.time()
print("Runtime of the program is", end - start)

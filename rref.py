# store the each row in matrix array
matrix = []
rows = int(raw_input("How many rows: "))
cols = int(raw_input("How many columns: "))

r = 0
while(r < rows):
    row = raw_input("[ M: {} row ]\n".format(r+1)).strip().split(" ")
    #Error check
    try:
        row = [int(i) for i in row] #row array
    except:
        print "Please enter numbers."
    if (len(row) == cols): #when you type 2 colums, then you have two elements
        matrix.append(row)
    else:
        print "Incorrect number of colums."
    r+=1
print(matrix)

# All zero rows, if any, are at the bottom of the matrix
# Each leading nonzero entry in a row is to the right of the leading nonzero entry
# in the preceding row
# Each pivot (leading nonzero entry) is equal to 1
# Each pivot is the only nonzero entry in its column

# Deal with each row i from 1 to n in turn,
# and work across the columns j from 1 to m
# skipping any column of all zero entries

# Find the next column j with a nonzero entry
# Interchange rows, if necessary, so that the pivot element A(i,j) is nonzero
# Make the pivot equal to 1 by dividing each element in the pivot row by the value of the pivot
# Make all elements above and below the pivot equal to 0 by substracting a
# suitable multiple of the pivot row from each other rows

# INPUT : m * n matrix A
# Set j <- 1
# For each row i from 1 to m do
    # While column j has all zero elements, set j <- j + 1. If j > n returns A
    # If element aij is zero, then Interchange row i with a row x> i that has axj not equal to nonzero
    # Divide each element of row i by aij, thus making the pivot aij equal to nonzero
    # For each row k from 1 to m with k is not equal to i, substract row i multiplied by akj from row k
# Return transformed matrix A
def ToReduceRowEcheloonForm(matrix):
    if not matrix:
        return
    lead = 0
    rowCount = rows
    columnCount = cols
    for r in range(0,rowCount):
        if lead >= columnCount:
            return
        i = r
        while matrix[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        matrix[i],matrix[r] = matrix[r],matrix[i]
        lv = matrix[r][lead]
        matrix[r] = [ mrx / float(lv) for mrx in matrix[r]]
        for i in range(rowCount):
            if i != r:
                lv = matrix[i][lead]
                matrix[i] = [ iv - lv*rv for rv,iv in zip(matrix[r],matrix[i])]
        lead += 1

ToReduceRowEcheloonForm(matrix)
print "OUPUT: Reduced Row Echeolon Form"
for rw in matrix:
    print "["+ ', '.join((str(rv) for rv in rw)) + "]"
    #
    # for r in range(rows):
    #     row = []
    #     for c in range(cols):
    #         row.append(int(input("M: {} -> R: {} C: {}\n>>>".format(r+1, r+1, c+1))))
    #         matrix.append(row)
    #

#
#
# Matrix Operations  
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

def mult_row(matrix, r, m):
    """Code for the function mult_row(matrix, r, m) that multiplies 
    row r of the specified matrix by the specified multiplier m. 
    """
    rows=len(matrix)
    columns=len(matrix[0])
    for a in range(rows):
        for b in range(columns):
            if a==r:
                matrix[a][b]*=m
                
def add_row_into(matrix, source, dest):
    """Code for the function add_row_into(matrix, source, dest)
    that takes the specified 2-D list matrix and adds each 
    element of the row with index source (the source row) to 
    the corresponding element of the row with index dest 
    (the destination row).
    """
    columns=len(matrix[0])
    for c in range(columns):
            matrix[dest][c]+=matrix[source][c]
            


def add_mult_row_into(matrix, m, source, dest):
    """Code for the function add_mult_row_into(matrix, m, source, dest) 
    that takes the specified 2-D list matrix and adds each element of 
    row source (the source row), multiplied by m, to the corresponding 
    element of row dest (the destination row). 
    """
    source_row=matrix[source]
    dest_row=matrix[dest]
    for i in range (len(source_row)):
        dest_row[i]+=((source_row[i]*m))
        

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def transpose(matrix):
    """function transpose(matrix) that takes the specified 2-D list 
    matrix and creates and returns a new 2-D list that is the 
    transpose of matrix.
    """
    rows=len(matrix)
    columns=len(matrix[0])
    
    new_matrix=create_grid(columns,rows)
    
    for r in range(rows):
        for c in range(columns):
            new_matrix[c][r]=matrix[r][c]
    return new_matrix
                
### Add your functions for options 2-5 here. ###

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
        elif choice == 2:
            r=int(input('Index of Row:'))
            m=float(input('Multiplier:'))
            mult_row(matrix,r,m)
        elif choice==3:
            source=int(input('Index of source row:'))
            dest=int(input('Index of destination row:'))
            add_row_into(matrix, source, dest)
        elif choice==4:
            m=float(input('Multiplier:'))
            source=int(input('Index of source row:'))
            dest=int(input('Index of destination row:'))
            add_mult_row_into(matrix, m, source, dest)
        elif choice==5:
            matrix=transpose(matrix)
            

        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

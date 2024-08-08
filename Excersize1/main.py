rows1 = int(input('please enter the number of rows for first matrix: '))
column1 = int(input('please enter the number of columns for first matrix: '))
rows2 = int(input('please enter the number of rows for second matrix: '))
column2 = int(input('please enter the number of columns for second matrix: '))
if column1 != rows2:
    print('The number of rows is not equal to the number of columns')

#define function for generate matrix
def get_matrix(row_of_matrix, column_of_matrix):
    matrix = []
    for i in range(row_of_matrix):
        result = []
        numbers = input(f'Enter row {i + 1} of the matrix, with {column_of_matrix} elements separated by spaces: ').split()
        for number in numbers:
            result.append(int(number))
        matrix.append(result)
    return matrix


matrix1 = get_matrix(rows1, column1)
matrix2 = get_matrix(rows2, column2)
result = [[0 for _ in range(column2)] for _ in range(rows1)]
#Multiply matrix
for i in range(rows1):
    for j in range(column2):
        for k in range(column1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for item in result:
    print(item)
for item in result:
    print(item)

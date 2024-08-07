rows1 = int(input('give me rows for first matrix'))
Column1 = int(input('give me colmuns for first matrix'))
rows2 = int(input('give me rows for second matrix'))
Column2 = int(input('give me columns second matrix'))
if Column1 != rows2:
    print('they cant multiply')
def get_matrix(number1, number2):
    matrix = []
    for i in range(number1):
        result = []
        numbers = input('Enter each rows').split()
        for number in numbers:
            result.append(int(number))
        matrix.append(result)
    return matrix



matrix1 = get_matrix(rows1, Column1)
matrix2 = get_matrix(rows2, Column2)
result = [[0 for _ in range(Column2)] for _ in range(rows1)]
for i in range(rows1):
    for j in range(Column2):
        for k in range(Column1):
            result[i][j] += matrix1[i][k] * matrix2[k][j]

for item in result:
    print(item)

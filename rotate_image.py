from time_of_function import benchmark


@benchmark
def rotate1(matrix):
    matrix = [list(reversed(x)) for x in zip(*matrix)]
    return matrix

@benchmark
def rotate2(matrix):
    for i in range(0, len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(0, len(matrix)):
        matrix[i].reverse()
    return matrix

len_matrix = 1000
nums = [num+1 for num in range(len_matrix**2)]
matrix = [[i for i in range(x*len_matrix-len_matrix+1, x*len_matrix+1)]
          for x in range(1, len_matrix+1)]
if rotate1(matrix) == rotate2(matrix):
    print('Ok', len_matrix)
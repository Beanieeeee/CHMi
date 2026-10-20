def file_op(name):
    with open(name, 'r') as f:
        n = int(f.readline())
        m = [list(map(float, f.readline().split())) for _ in range(n)]
        v = list(map(float, f.readline().split()))
    return n, m, v


def null_Matrix(n):
    return [[0 for _ in range(n)] for _ in range(n)]


def ed_Matrix(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]


def matrix_mult(M1, M2, n):
    M = null_Matrix(n)
    for i in range(n):
        for j in range(n):
            for t in range(n):
                M[i][j] += M1[i][t] * M2[t][j]
    return M


def copy_matrix(M1):
    n = len(M1)
    return [[M1[i][j] for j in range(n)] for i in range(n)]


def matrix_vector_mult(M, V, n):
    res = [0.0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            res[i] += M[i][j] * V[j]

    return res

def matrix_equal(M1, M2):
    n = len(M1)
    if len(M1) != len(M2):
        return False
    for i in range(n):
        for j in range(n):
            if abs(M1[i][j] - M2[i][j]) > 1e-9:
                return False
    return True

def print_matrix(matrix, name=''):
    if name != '':
        print(name)
    for row in matrix:
        print(row)
    print()


def solution_forw(A, b):
    n = len(A)
    for i in range(n):
        for j in range(i):
            b[i] -= A[i][j] * b[j]
    return b


def solution_back(A, b):
    n = len(A)
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            b[i] -= A[i][j] * b[j]
        b[i] /= A[i][i]
    return b

def det(U, count):
    det = 1.0
    for i in range(len(U)):
        det *= U[i][i]
    if count % 2 != 0:
        det *= -1
    return det


def LU(U, n):
    count = 0
    L = ed_Matrix(n)
    P = ed_Matrix(n)

    for k in range(0, n - 1):

        pivot_row = k

        for i in range(k, n):
            if (abs(U[i][k])) > abs(U[pivot_row][k]):
                pivot_row = i

        if abs(U[pivot_row][k]) < 1e-9:
            return

        if pivot_row != k:
            U[k], U[pivot_row] = U[pivot_row], U[k]
            P[k], P[pivot_row] = P[pivot_row], P[k]

            for j in range(k):
                L[k][j], L[pivot_row][j] = L[pivot_row][j], L[k][j]

            count += 1

        for i in range (k + 1, n):
            mult = U[i][k]/U[k][k]
            L[i][k] = mult
            for j in range (k, n):
                U[i][j] = U[i][j] -  mult * U[k][j]
    return L, U, P, count


def solve_LU(L, U, P, b, n):
    Pb = matrix_vector_mult(P, b, n)
    y = solution_forw(L, Pb)
    x = solution_back(U, y)

    return x

def inv_matrix(L, U, P, n):
    E = ed_Matrix(n)
    A_inv = null_Matrix(n)

    for j in range(n):
        e = [E[i][j] for i in range(n)]
        x = solve_LU(L, U, P, e, n)
        for i in range(n):
            A_inv[i][j] = x[i]

    return A_inv



n, m, v = file_op('1laba.txt')

if __name__ == '__main__':
    n, m, v = file_op('1laba.txt')

    U = copy_matrix(m)
    L, U, P, count = LU(U, n)

    print_matrix(m, 'Исходная матрица:')
    print_matrix(L, 'L:')
    print_matrix(U, 'U:')
    print_matrix(P, 'P:')

    LU_result = matrix_mult(L, U, n)
    PA_result = matrix_mult(P, m, n)

    print_matrix(LU_result, 'L * U:')
    print_matrix(PA_result, 'P * A:')

    print('L * U = P * A:', matrix_equal(LU_result, PA_result))

    x = solve_LU(L, U, P, v, n)
    print('Решение:', x)

    A_inv = inv_matrix(L, U, P, n)
    print_matrix(A_inv, 'Обратная матрица:')

    check = matrix_mult(m, A_inv, n)
    print('A * A^-1 = E:', matrix_equal(check, ed_Matrix(n)))

    print('Определитель:', det(U, count))
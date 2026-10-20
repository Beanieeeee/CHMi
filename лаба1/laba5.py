import math
from laba1 import ed_Matrix, copy_matrix, matrix_mult

def file_op(name):
    with open(name, 'r') as f:
        n = int(f.readline())
        A = [list(map(float, f.readline().split())) for _ in range(n)]
    return n, A

def QR(A):
    n = len(A)

    Q = ed_Matrix(n)
    R = copy_matrix(A)

    for j in range(n):
        for i in range(n - 1, j, -1):
            a = R[i - 1][j]
            b = R[i][j]

            r = math.sqrt(a*a + b*b)

            if r == 0:
                continue

            c = a / r
            s = b / r

            for k in range(n):
                x = R[i - 1][k]
                y = R[i][k]

                R[i - 1][k] = c*x + s*y
                R[i][k] = -s*x + c*y

            for k in range(n):
                x = Q[k][i - 1]
                y = Q[k][i]

                Q[k][i - 1] = c*x + s*y
                Q[k][i] = -s*x + c*y

    return Q, R


def matrix_error(A):
    n = len(A)
    s = 0

    for i in range(1, n):
        for j in range(i):
            s += A[i][j] ** 2

    return math.sqrt(s)

def QR_method(A, eps):
    n = len(A)
    count = 0

    while matrix_error(A) > eps:
        Q, R = QR(A)
        A = matrix_mult(R, Q, n)

        count += 1

        if count > 10000:
            print('Метод не сошелся')
            break

    return A, count


n, A = file_op('5laba.txt')
print('Исходная матрица:')
for row in A:
    print(row)

Q, R = QR(A)

print('Матрица Q:')
for row in Q:
    print(row)
print('Матрица R:')
for row in R:
    print(row)

print('Проверка Q * R:')
B = matrix_mult(Q, R, n)

for row in B:
    print(row)


for eps in [0.01, 0.0001, 0.000001]:
    B = copy_matrix(A)
    D, count = QR_method(B, eps)
    print('Точность:', eps)
    print('Итераций:', count)

    print('Собственные значения:')
    for i in range(n):
        print(D[i][i])

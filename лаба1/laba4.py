import math
from laba1 import ed_Matrix, copy_matrix


def file_op(name):
    with open(name, 'r') as f:
        n = int(f.readline())
        A = [list(map(float, f.readline().split())) for _ in range(n)]
    return n, A

def matrix_error(A):
    n = len(A)
    s = 0

    for i in range(n):
        for j in range(i + 1, n):
            s += A[i][j] ** 2

    return math.sqrt(s)

def rotation(A, eps):
    n = len(A)
    V = ed_Matrix(n)
    count = 0

    while matrix_error(A) > eps:
        p = 0
        q = 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > abs(A[p][q]):
                    p = i
                    q = j

        angle = 0.5 * math.atan2(2 * A[p][q], A[p][p] - A[q][q])

        c = math.cos(angle)
        s = math.sin(angle)

        a = A[p][p]
        b = A[q][q]
        d = A[p][q]

        A[p][p] = c*c*a + 2*c*s*d + s*s*b
        A[q][q] = s*s*a - 2*c*s*d + c*c*b

        A[p][q] = 0
        A[q][p] = 0

        for i in range(n):
            if i != p and i != q:
                a = A[i][p]
                b = A[i][q]

                A[i][p] = c*a + s*b
                A[p][i] = A[i][p]

                A[i][q] = -s*a + c*b
                A[q][i] = A[i][q]

            a = V[i][p]
            b = V[i][q]

            V[i][p] = c*a + s*b
            V[i][q] = -s*a + c*b
        count += 1
    return A, V, count


n, A = file_op('4laba.txt')

for eps in [0.01, 0.0001, 0.000001]:
    B = copy_matrix(A)

    D, V, count = rotation(B, eps)

    print('Точность:', eps)
    print('Количество итераций:', count)

    print('Собственные значения:')
    for i in range(n):
        print(D[i][i])

    print('Собственные векторы:')
    for i in range(n):
        v = [V[j][i] for j in range(n)]
        print(v)

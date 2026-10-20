from laba1 import file_op


def iterations(A, b, eps):
    n = len(A)
    x = [0.0 for _ in range(n)]
    count = 0
    while True:
        count += 1
        new_x = [0.0 for _ in range(n)]

        for i in range(n):
            s = 0

            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            new_x[i] = (b[i] - s) / A[i][i]

        error = 0

        for i in range(n):
            if abs(new_x[i] - x[i]) > error:
                error = abs(new_x[i] - x[i])

        x = new_x

        if error < eps:
            break

        if count > 10000:
            print('Метод не сошелся')
            return x, count

    return x, count


def seidel(A, b, eps):
    n = len(A)
    x = [0.0 for _ in range(n)]
    count = 0

    while True:
        count += 1
        old_x = x.copy()

        for i in range(n):
            s = 0

            for j in range(n):
                if i != j:
                    s += A[i][j] * x[j]

            x[i] = (b[i] - s) / A[i][i]

        error = 0

        for i in range(n):
            if abs(x[i] - old_x[i]) > error:
                error = abs(x[i] - old_x[i])
        if error < eps:
            break

        if count > 10000:
            print('Метод не сошелся')
            return x, count

    return x, count


def check(A, b, x):
    n = len(A)
    error = 0

    for i in range(n):
        s = 0
        for j in range(n):
            s += A[i][j] * x[j]
        if abs(s - b[i]) > error:
            error = abs(s - b[i])

    return error

n, A, b = file_op('3laba.txt')
eps = 0.0001

x1, count1 = iterations(A, b, eps)
x2, count2 = seidel(A, b, eps)

print('Метод простых итераций:')
print('x =', x1)
print('Итераций:', count1)
print('Невязка:', check(A, b, x1))

print('Метод Зейделя:')
print('x =', x2)
print('Итераций:', count2)
print('Невязка:', check(A, b, x2))

print('Сравнение точности:')

for eps in [0.01, 0.0001, 0.000001]:
    x1, count1 = iterations(A, b, eps)
    x2, count2 = seidel(A, b, eps)

    print('eps =', eps)
    print('Простые итерации:', count1)
    print('Зейдель:', count2)

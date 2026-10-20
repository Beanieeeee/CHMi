def file_op(name):
    with open(name, 'r') as f:
        n = int(f.readline())

        low = [0.0 for _ in range(n)]
        main = [0.0 for _ in range(n)]
        high = [0.0 for _ in range(n)]

        for i in range(n):
            row = list(map(float, f.readline().split()))

            main[i] = row[i]
            if i > 0:
                low[i] = row[i - 1]
            if i < n - 1:
                high[i] = row[i + 1]
        rhs = list(map(float, f.readline().split()))
    return n, low, main, high, rhs


def sweep(n, low, main, high, rhs):
    P = [0.0 for _ in range(n)]
    Q = [0.0 for _ in range(n)]

    P[0] = -high[0] / main[0]
    Q[0] = rhs[0] / main[0]

    for i in range(1, n):

        denom = main[i] + low[i] * P[i - 1]

        P[i] = -high[i] / denom

        Q[i] = (rhs[i] - low[i] * Q[i - 1]) / denom

    x = [0.0 for _ in range(n)]
    x[n - 1] = Q[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = P[i] * x[i + 1] + Q[i]

    return P, Q, x


n, low, main, high, rhs = file_op('2laba.txt')

P, Q, x = sweep(n, low, main, high, rhs)


print("Коэффициенты прогонки:")

for i in range(n):
    print(f"i = {i + 1}: P = {P[i]:.6f}, Q = {Q[i]:.6f}")

print("low =", low)
print("main =", main)
print("high =", high)
print("rhs =", rhs)

print("\nРешение:")

for i in range(n):
    print(f"x{i + 1} = {x[i]:.6f}")
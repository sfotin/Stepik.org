n, m, k, x, y, z, t, a = [int(input()) for _ in range(8)]
x1 = m + n - t - x  # прочитали только 1 и 2
y1 = m + k - t - y  # прочитали только 2 и 3
z1 = k + n - t - z  # прочитали только 3 и 1
n1 = n - x1 - z1 - t  # прочитали только 1
m1 = m - x1 - y1 - t  # прочитали только 2
k1 = k - y1 - z1 - t  # прочитали только 3
print(n1 + m1 + k1)  # прочитали только одну
print(x1 + y1 + z1)  # прочитали по две
print(a - (n1 + m1 + k1 + x1 + y1 + z1 + t))  # ничего не читали

N = int(input("Введите размер списка: "))
a = []

print("Введите элементы списка:")
for i in range(N):
    a.append(int(input()))

for i in range(1, N - 1):
    if a[i] < a[i - 1] and a[i] < a[i + 1]:
        a[i] = a[i] ** 2

print("Результирующий список:", a)

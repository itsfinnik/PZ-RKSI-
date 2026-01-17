N = int(input("Введите размер списка: "))
a = []

print("Введите элементы списка:")
for i in range(N):
    a.append(int(input()))

local_max = []

for i in range(1, N - 1):
    if a[i] > a[i - 1] and a[i] > a[i + 1]:
        local_max.append(a[i])

if local_max:
    print("Минимальный локальный максимум:", min(local_max))
else:
    print("Локальных максимумов нет")

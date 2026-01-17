a = []
print("Введите 10 целых чисел:")
for i in range(10):
    a.append(int(input()))

odd_numbers = []

for i in range(10):
    if a[i] % 2 != 0:
        odd_numbers.append(a[i])

print("Нечётные числа:", odd_numbers)
print("Количество нечётных чисел K =", len(odd_numbers))

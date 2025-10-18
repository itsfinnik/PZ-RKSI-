n = int(input())
m = float(input())

if n == 1:
    result = m
elif n == 2:
    result = m / 1000000
elif n == 3:
    result = m / 1000
elif n == 4:
    result = m * 1000
elif n == 5:
    result = m * 100

print(result)
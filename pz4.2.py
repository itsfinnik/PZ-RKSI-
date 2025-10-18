P = float(input())
day_distance = 10
total_distance = 10
K = 1

while total_distance <= 200:
    day_distance += day_distance * (P / 100)
    total_distance += day_distance
    K += 1

print(K)
print(round(total_distance, 2))
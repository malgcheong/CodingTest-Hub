n = int(input())
result = 1 # 0!
for i in range(n, 1, -1):
    result *= i
print(result)
n = int(input())

i = 1

while i <= n:
    if i ** 2 > n:
        break
    i += 1

print(i)

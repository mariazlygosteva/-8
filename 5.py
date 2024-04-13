def perfect_number(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

N = int(input())
perfect_count = 0

for i in range(2, N+1):
    if perfect_number(i):
       perfect_count += 1

print(perfect_count)
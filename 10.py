N = int(input("Введите число N: "))

for num in range(2, N+1):
    sum_divisors = 1
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            sum_divisors += i
    if sum_divisors == num:
        print(num)
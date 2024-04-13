def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers_up_to_n(n):
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

N = int(input("Введите число N: "))
primes = prime_numbers_up_to_n(N)

print("Простые числа до", N, ":", primes)
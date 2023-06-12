def sum_of_divisors(n):
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum

def find_friendly_numbers(k):
    friendly_pairs = []
    for n in range(1, k+1):
        m = sum_of_divisors(n)
        if m > n and sum_of_divisors(m) == n:
            friendly_pairs.append((n, m))
    return friendly_pairs

k = int(input("Введите число k: "))

pairs = find_friendly_numbers(k)
for pair in pairs:
    print(pair[0], pair[1])

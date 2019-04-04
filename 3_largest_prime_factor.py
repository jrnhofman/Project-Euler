import numpy as np


def is_prime(x):

    if x % 2 == 0:
        return False

    m = x/2 - 0.5 if ((x/2 - 0.5) % 2 == 1) else x/2 - 1.5
    while m > 1:
        if x % m == 0:
            return False
        m = m - 2

    return True


def get_primes(n):

    return [x for x in range(n) if is_prime(x)]


def get_largest_prime_factor(n):

    primes_reverse = get_primes(n)[::-1]

    prime_factors = []
    for p in primes_reverse:

        remaining_factor = float(n)/p
        if remaining_factor != int(remaining_factor):
            continue
        else:
            n = remaining_factor
            prime_factors.append(p)

    return prime_factors


print(get_largest_prime_factor(600851475143))

def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

if __name__ == "__main__":
    number = 600851475143
    result = largest_prime_factor(number)
    print("Largest prime factor of 600851475143:", result)


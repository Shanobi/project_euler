def sum_even_terms(limit):
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

if __name__ == "__main__":
    result = sum_even_terms(4000000)
    print("Sum of even terms in Fibonacci seq. below 4 million:", result)


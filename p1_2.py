def sum_of_multiples(limit):
    return sum(num for num in range(limit) if num % 3 == 0 or num % 5 == 0)

if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print("Sum of multiples of 3 or 5 below 1000:", result)


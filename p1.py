def sum_of_multiples(limit):
    total = 0
    count = 1
    while count < limit:
        if count % 3 == 0 or count % 5 == 0:
            total += count
        count += 1
    return total

if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print("Sum of multiples of 3 or 5 below 1000:", result)

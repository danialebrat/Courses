def algorithm(n):
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

        sequence.append(n)

    return sequence


# Read the input
n = int(input())

# Call the algorithm function
sequence = algorithm(n)

# Print the sequence
print(" ".join(str(num) for num in sequence))

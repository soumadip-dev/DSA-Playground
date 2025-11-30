# def countDigits(n):
#     count = 0
#     n = str(n)
#     while count < len(n):
#         count += 1
#     print(count)

# countDigits(4578)


def count_digits(n):
    # Convert negative number to positive
    n = abs(n)

    # If n = 0, digit count is 1
    if n == 0:
        return 1
    else:
        digit_count = 0
        while n != 0:
            n = n // 10
            digit_count += 1
    return digit_count


print(count_digits(-500))

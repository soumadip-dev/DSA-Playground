# def countDigits(n):
#   count = 0
#   n = str(n)
#   while count < len(n):
#     count+=1
#   print(count)

# countDigits(4578)


def countDigits(n):
    # Converting negative to positive
    n = abs(n)

    # if n = 0 it will return 1
    if n == 0:
        return 1
    else:
        count = 0
        while n != 0:
            n = n // 10
            count += 1
    return count


print(countDigits(-500))

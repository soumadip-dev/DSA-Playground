def reverse(x):
    reversed_number = 0
    original_number = x
    limit = 2**31

    x = abs(x)

    while x > 0:
        reversed_number = reversed_number * 10 + (x % 10)
        x //= 10

    # 32-bit signed integer range: −2^31 to 2^31 − 1
    if reversed_number < -limit or reversed_number > limit - 1:
        return 0

    return -reversed_number if original_number < 0 else reversed_number


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))

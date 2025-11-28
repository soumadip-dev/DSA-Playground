def reverse(x):
    reversed_num = 0
    original = x
    limit = 2 ** 31
    x = abs(x)
    while x > 0:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    
    if reversed_num < -limit or reversed_num > limit:
        return 0
    return -reversed_num if original < 0 else reversed_num


print(reverse(123))
print(reverse(-123))
print(reverse(120))
print(reverse(1534236469))
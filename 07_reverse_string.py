# Reverse a list of characters in place using two-pointer technique


def reverse_string(s):
    """
    Reverses the list of characters in place using two pointers.
    """
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        s[left_index], s[right_index] = s[right_index], s[left_index]
        left_index += 1
        right_index -= 1

    return s


def reverse_string_better_way(s):
    """
    Reverses the list of characters in place by swapping
    elements up to the halfway point.
    """
    for i in range(len(s) // 2):
        s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]

    return s


print(reverse_string(["h", "e", "l", "l", "o"]))
print(reverse_string_better_way(["H", "a", "n", "n", "a", "h"]))

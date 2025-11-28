def second_largest_number(array):
    if len(array) < 2:
        return None
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(len(array)):
        if array[i] > largest:
            second_largest = largest
            largest = array[i]
        elif array[i] > second_largest and array[i] != largest:
            second_largest = array[i]
    return second_largest


print(second_largest_number([1, 5, 4, 3, 7, 9, 9]))
print(second_largest_number([1]))

def second_largest_number(nums):
    """
    Returns the second largest distinct number in the list.
    If fewer than two distinct elements exist, returns None.
    """
    if len(nums) < 2:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    for i in range(len(nums)):
        if nums[i] > largest:
            second_largest = largest
            largest = nums[i]
        elif nums[i] > second_largest and nums[i] != largest:
            second_largest = nums[i]

    return second_largest


print(second_largest_number([1, 5, 4, 3, 7, 9, 9]))
print(second_largest_number([1]))

# Remove all occurrences of a specific value from the array in-place
# Returns the count of elements that are not equal to the given value.


def remove_element(nums, val):
    """
    Removes all occurrences of 'val' from the list in place.
    Returns the number of elements that are not equal to 'val'.
    """
    if not nums:
        return 0

    write_index = 0

    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))

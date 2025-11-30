# Increasing order:        nums[i+1] > nums[i]
# Decreasing order:        nums[i+1] < nums[i]
# Non-decreasing order:    nums[i+1] >= nums[i]    # duplicates allowed


# Easy approach — Space Complexity: O(N)
def remove_duplicates_using_extra_array(nums):
    """
    Removes consecutive duplicate elements from a sorted list.
    Returns a new list without modifying the original.
    """
    if not nums:
        return []

    unique_elements = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != unique_elements[-1]:
            unique_elements.append(nums[i])

    return unique_elements


result1 = remove_duplicates_using_extra_array([5, 5, 7, 8, 8, 8, 9, 9, 10, 10])
print(result1)


# In-place approach — Space Complexity: O(1)
def remove_duplicates_in_place(nums):
    """
    Removes consecutive duplicate elements from a sorted list in place.
    Returns the list of unique elements (up to the updated size).
    """
    if not nums:
        return []

    write_index = 0

    for read_index in range(1, len(nums)):
        if nums[read_index] > nums[write_index]:
            write_index += 1
            nums[write_index] = nums[read_index]

    # Return the list up to write_index (inclusive)
    return nums[: write_index + 1]


result2 = remove_duplicates_in_place([5, 5, 7, 8, 8, 8, 9, 9, 10, 10])
print(result2)

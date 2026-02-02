def nextGreatestLetter(letters, target):
    """
    Given a sorted array of characters letters that is sorted in non-decreasing order,
    and a character target, return the smallest character in letters that is
    lexicographically greater than target. If such a character does not exist,
    return the first character in letters.

    Time complexity: O(log n)
    """
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    # After the loop, left is the insertion point
    if left < len(letters):
        return letters[left]
    else:
        return letters[0]

# Example usage:
if __name__ == "__main__":
    print(nextGreatestLetter(["c","f","j"], "a"))  # Output: "c"
    print(nextGreatestLetter(["c","f","j"], "c"))  # Output: "f"
    print(nextGreatestLetter(["x","x","y","y"], "z"))  # Output: "x"

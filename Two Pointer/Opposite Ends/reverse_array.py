"""
Problem:
    We have an array or string we need to reverse it.
"""

def reverse_array(arr:list) -> list:
    left , right = 0, len(arr)-1
    while left < right:
        temp = arr[left]
        arr[left], arr[right] = arr[right], temp
        left += 1 ; right -= 1
    return arr


if __name__ == "__main__":
    print(reverse_array([2,3,8,4,9]))

"""
Time Complexity:
    O(n/2) = O(n)
Space Complexity:
    O(1)
"""
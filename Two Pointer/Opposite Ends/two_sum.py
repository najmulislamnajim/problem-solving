"""
Problem:
Given a sorted array of integers and a target value, find the indices (1-based) of two numbers that add up to the target. Assume exactly one solution exists, and you cannot use the same element twice.

Example
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: 2 + 7 = 9, and those are at indices 1 and 2 (1-based).
"""

def solve(nums,target):
    left,right=0,len(nums)-1
    while left<right:
        if nums[left] + nums[right] == target:
            return [left+1, right+1] # 1-based index
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

if __name__ == "__main__":
    result = solve([2, 7, 11, 15], 9)
    print(result)
    
"""
Time Complexity:
    O(n) — In the worst case, one of the pointers will traverse to the end of the array.

Space Complexity:
    O(1) — Only a constant amount of extra memory is used.
"""

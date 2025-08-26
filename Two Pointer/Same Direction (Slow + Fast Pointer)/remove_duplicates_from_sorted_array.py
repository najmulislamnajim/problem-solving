""" 
Problem:
    Remove Duplicates from Sorted Array.
Link:
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
Input:
    nums = [0,0,1,1,1,2,2,3,3,4]
Output:
    5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

from typing import List
def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    
    slow = 0
    
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            slow += 1
            nums[slow] = nums[fast]
            
    return slow+1


if __name__ == "__main__":
    
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = removeDuplicates(nums)
    print(k)
    for i in range(k):
        print(nums[i], end = " ")
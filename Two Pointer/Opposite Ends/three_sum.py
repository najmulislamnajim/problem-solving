""" 
Problem
    Given an array of integers, find all unique triplets (three numbers) in the array which sum to zero. The solution set must not contain duplicate triplets.
Link
    https://leetcode.com/problems/3sum/description/

Example
    Input: arr = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]] 
    Triplets must not repeat – order doesn’t matter.
"""
from typing import List
def solve(arr:List[int]) -> List[List[int]]:
    arr.sort()
    n = len(arr)
    res = []
    for i in range(n):
        
        if i>0 and arr[i] == arr[i-1]:
            continue # Skip duplicate, since it already added.
        
        left, right, target = i+1 , n-1, -arr[i]
        
        while left < right:
            if arr[left] + arr[right] == target:
                res.append([arr[i], arr[left], arr[right]])
                # Skip Duplicate for Second Number.
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                # Skip Duplicate for Third Number.
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
                    
                left +=1 ; right -= 1
            elif arr[left] + arr[right] > target:
                right -= 1
            else:
                left += 1           
    return res
    
if __name__ == "__main__":
    print(solve([-1, 0, 1, 2, -1, -4]))

""" 
Time Complexity:
    O(n^2)
    
Space Complexity:
    O(k) : k triplets(output array)
"""
        
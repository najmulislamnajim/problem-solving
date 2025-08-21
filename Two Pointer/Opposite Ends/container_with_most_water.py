""" 
Problem:
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.
"""

# Solve
from typing import List
def maxArea(height: List[int]) -> int:
    left , right , max_area = 0 , len(height)-1 , 0
    while left<right:
        area = min(height[left],height[right])*(right-left)
        max_area = max(max_area,area)
        if height[left]>height[right]:
            right -=1
        else:
            left+=1    
    return max_area

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))  # 49
    print(maxArea([1,1]))  # 1
    print(maxArea([4,3,2,1,4]))  # 16
    
""" 
Time Complexity:
    O(n) : n is the length of height array.
Space Complexity:
    O(1) : No extra space used.
"""
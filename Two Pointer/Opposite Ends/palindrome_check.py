""" 
Problem:
    Given a string, we need to find is it a palindrome or not.
"""

def solve (s):
    left , right = 0, len(s)-1
    while left < right :
        if s[left] != s[right] :
            return False 
        left += 1
        right -= 1
    return True
        
if __name__ == "__main__":
    print(solve("amma"))
    print(solve("mother"))
    
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
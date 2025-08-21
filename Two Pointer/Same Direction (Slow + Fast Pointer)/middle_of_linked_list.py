""" 
Problem:
    Find the middle of a linked list using the slow and fast pointer technique.
Link: 
    https://leetcode.com/problems/middle-of-the-linked-list/description/
Input:
    head = [1,2,3,4,5]
Output:
    [3]
"""

# Solve
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    middle = middleNode(head)
    print(middle.val)  # Output: 3

"""
Time Complexity:
    O(n) : n is the number of nodes in the linked list.
Space Complexity:
    O(1) : No extra space used.
"""
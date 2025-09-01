""" 
Problem:
    141. Linked List Cycle
Link:
    https://leetcode.com/problems/linked-list-cycle/description/
Description:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Return true if there is a cycle in the linked list. Otherwise, return false.
"""
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next 

    print(hasCycle(head))  
    
""" 
Time Complexity:
    O(N)
Space Complexity:
    O(1)
"""
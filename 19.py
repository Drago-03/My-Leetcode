#19. Remove Nth Node From End of List

"""Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, one ahead of the other by n nodes
        ahead = head
        behind = head
        for _ in range(n):
            ahead = ahead.next
        # If ahead reaches the end, it means the node to be removed is the head
        if ahead is None:
            return head.next
        # Move both pointers until ahead reaches the end
        while ahead.next:
            ahead = ahead.next
            behind = behind.next
        # Remove the nth node from the end
        behind.next = behind.next.next
        return head
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1: The picture
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.'''
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop through both linked lists
        while l1 is not None or l2 is not None:
            # If a list ends early, treat the value as 0
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Sum the current digits and the carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            # Move to the next node in both lists
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's a carry left after the final digit
        if carry > 0:
            current.next = ListNode(carry)
        
        # The result is the next node of dummy_head
        return dummy_head.next

# Helper function to create linked list from a list of integers
def create_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

# Helper function to convert a linked list to a Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example usage
l1 = create_linked_list([2, 4, 3])  # represents 342
l2 = create_linked_list([5, 6, 4])  # represents 465

solution = Solution()
result_node = solution.addTwoNumbers(l1, l2)

# Convert the result linked list to a list for output
result_as_list = linked_list_to_list(result_node)
print("Resulting linked list as list:", result_as_list)

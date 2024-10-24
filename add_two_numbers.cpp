/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */


/*You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

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
    It is guaranteed that the list represents a number that does not have leading zeros.*/

#include <cstddef>
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0); // Create a dummy head for result list
        ListNode* current = dummyHead;         // Pointer to track current node in result list
        int carry = 0;                         // Variable to store carry

        // Loop through both lists until both are exhausted
        while (l1 != NULL || l2 != NULL) {
            int x = (l1 != NULL) ? l1->val : 0; // Get value from l1 or 0 if l1 is exhausted
            int y = (l2 != NULL) ? l2->val : 0; // Get value from l2 or 0 if l2 is exhausted
            int sum = carry + x + y;            // Calculate sum of values and carry
            carry = sum / 10;                   // Calculate new carry
            current->next = new ListNode(sum % 10); // Create a new node for the current digit
            current = current->next;            // Move to the next node
            
            // Move to the next nodes in l1 and l2 if available
            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
        }

        // If there's any carry left after the last iteration, add a new node for it
        if (carry > 0) {
            current->next = new ListNode(carry);
        }

        return dummyHead->next;  // Return the resulting list, excluding the dummy head
    }
};
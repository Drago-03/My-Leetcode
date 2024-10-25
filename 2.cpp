// 2. Add Two Numbers

/*
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

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
    It is guaranteed that the list represents a number that does not have leading zeros.
*/

#include <iostream>
#include <vector>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummy_head = new ListNode(0);
        ListNode* current = dummy_head;
        int carry = 0;
        
        // Loop through both linked lists
        while (l1 != nullptr || l2 != nullptr) {
            // If a list ends early, treat the value as 0
            int val1 = (l1 != nullptr) ? l1->val : 0;
            int val2 = (l2 != nullptr) ? l2->val : 0;
            
            // Sum the current digits and the carry
            int total = val1 + val2 + carry;
            carry = total / 10;
            current->next = new ListNode(total % 10);
            current = current->next;
            
            // Move to the next node in both lists
            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }
        
        // If there's a carry left after the final digit
        if (carry > 0) {
            current->next = new ListNode(carry);
        }
        
        // The result is the next node of dummy_head
        ListNode* result = dummy_head->next;
        delete dummy_head;
        return result;
    }
};

// Helper function to create linked list from a vector of integers
ListNode* createLinkedList(const std::vector<int>& nums) {
    if (nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* current = head;
    for (size_t i = 1; i < nums.size(); ++i) {
        current->next = new ListNode(nums[i]);
        current = current->next;
    }
    return head;
}

// Helper function to convert a linked list to a vector
std::vector<int> linkedListToVector(ListNode* node) {
    std::vector<int> result;
    while (node) {
        result.push_back(node->val);
        node = node->next;
    }
    return result;
}

// Helper function to delete a linked list
void deleteLinkedList(ListNode* head) {
    while (head) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

int main() {
    std::vector<int> nums1 = {2, 4, 3};  // represents 342
    std::vector<int> nums2 = {5, 6, 4};  // represents 465

    ListNode* l1 = createLinkedList(nums1);
    ListNode* l2 = createLinkedList(nums2);

    Solution solution;
    ListNode* result_node = solution.addTwoNumbers(l1, l2);

    // Convert the result linked list to a vector for output
    std::vector<int> result_as_vector = linkedListToVector(result_node);
    
    std::cout << "Resulting linked list as vector: ";
    for (int num : result_as_vector) {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    // Clean up memory
    deleteLinkedList(l1);
    deleteLinkedList(l2);
    deleteLinkedList(result_node);

    return 0;
}

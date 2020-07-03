#include <iostream>

//  Definition for singly-linked list.
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
        ListNode* result;
        ListNode** head = &result;
        (*head)->next = result;
        int carry = 0;
        int sum = 0;
        while(l1 != nullptr || l2 != nullptr){
            sum = l1->val + l2->val + carry;
            if(sum >= 10){
                result->next = new ListNode(sum - 10);
                carry = 1;
            }
            else{
                result->next = new ListNode(sum);
                carry = 0;
            }
            l1 = l1->next;
            l2 = l2->next;
            result = result->next;
        }
        *head = (*head)->next;
        return *head;
    }
};
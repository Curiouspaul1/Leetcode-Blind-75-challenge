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
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* temp = head;
        int len=0;
        while(temp != NULL){
            temp = temp->next;
            len++;
        }
        len = len - n;
        
        ListNode* tem = new ListNode();
        tem->next = head;
        ListNode* prev = tem;
        
        while(len--){
            prev = prev->next;
        }
        prev->next = prev->next->next;
        return tem->next;
    }
};

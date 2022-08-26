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
    ListNode* reverseList(ListNode* head) {
        // if(head->next == NULL) return head;
        // ListNode *current = head;
        // ListNode *next = NULL, *prev = NULL;
        // while(current != NULL) {
        //     next = current->next;
        //     prev = current;
        //     current = next;            
        // }
        // // head = prev;
        // return prev;
        ListNode* prevNode = NULL;
        while(head)
        {
            ListNode* nextNode = head -> next ;
            head -> next = prevNode ;
            prevNode = head ;
            head = nextNode ;
        }
        return prevNode ;
    }
};

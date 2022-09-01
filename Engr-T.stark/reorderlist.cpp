class Solution {
public:
    void reorderList(ListNode* head) {
        
//      step 1 : Finding the middle of the list in order to split it in 2 parts
        ListNode *slow=head;
        ListNode *fast=head->next;
        
        while(fast&&fast->next)
        {
        slow=slow->next;
        fast=fast->next->next;
        }
        
        ListNode *head2=slow->next;
        slow->next=NULL;
        
//      step 2 : Reversing the 2nd half of the list
        ListNode *forward=NULL;
        ListNode *prev=NULL;
        ListNode *curr=head2;
        
        while(curr)
        {
            forward=curr->next;
            curr->next=prev;
            prev=curr;
            curr=forward;
        }
        
//       Step 3 : Merge the 2 lists 
        head2=prev;
        while(head2)
        {
            ListNode *ptr1=head->next;
            ListNode *ptr2=head2->next;
            
            head->next=head2;
            head2->next=ptr1;
            head=ptr1;
            head2=ptr2;
            
        }
    }
};

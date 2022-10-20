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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        int n = lists.size();
	// if size of lists is zero then return zero.
    if(n == 0)
    {
        return NULL;
    }
	// initialize min heap/ min(priority queue). 
    priority_queue<int,vector<int>,greater<int>>pq;
    int i;
	
    for(i=0;i<n;i++)
    {
        ListNode* temp = lists[i];
        while(temp != NULL)
        {
            pq.push(temp->val);
            temp = temp->next;
        }
    }
  ListNode* start = new ListNode(0);
    ListNode* head = start;
    while(!pq.empty())
    {
        head->next = new ListNode(pq.top());
        pq.pop();
        head = head->next;
    }
    return start->next;
    }
};

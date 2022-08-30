class cmp {
public:
bool operator()(ListNode*a ,ListNode* b){
    return a->val>b->val;
}
};

class solution {
    public:
    mergeKSortedLists(vector<ListNode*> &lists)
    {
      priority_queue<ListNode*,vector<ListNode*>,cmp> q;
    ListNode* dummy=new ListNode(-1);
    ListNode* tail=dummy;
    for(int i=0;i<lists.size();i++){
        if(lists[i] != NULL){
            q.push(lists[i]);
        }
    }
    while(q.size()){
        ListNode* temp=q.top();
        tail->next=temp;
        tail=temp;
        q.pop();
        if(temp->next != NULL){
            q.push(temp->next);
        }
    }
    return dummy->next;
    }
};

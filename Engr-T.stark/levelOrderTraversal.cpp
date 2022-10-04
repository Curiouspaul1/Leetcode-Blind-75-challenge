queue<TreeNode*> q;
    q.push(root);
    q.push(NULL);
    vector<vector<int>> ans;
    vector<int> t;
    
    
    if(root==NULL)
    {
        return ans;
    }
    
    while(!q.empty())
    {
        TreeNode* temp =q.front();
        q.pop();
        
        if(temp==NULL)
        {   
            ans.push_back(t);
            t.clear();
            if(!q.empty())
            {
                q.push(NULL);
            }
        }
        else  //temp != null
        {
            t.push_back(temp->val);
            
            if(temp->left!=NULL)
            {
                q.push(temp->left);
            }
            if(temp->right!=NULL)
            {
                q.push(temp->right);
            }
        }
    }
    
    return ans;

vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
 
        vector<vector<int>> ans;
        int fN=firstList.size();
        int sN=secondList.size();
        
        int i=0,j=0;
        
        
        while(i<fN and j<sN){
            
            // Case 2
            if(max(firstList[i][0],secondList[j][0])<=min(firstList[i][1],secondList[j][1])){
                ans.push_back({max(firstList[i][0],secondList[j][0]),min(firstList[i][1],secondList[j][1])});
            }
            
            if(firstList[i][1]>=secondList[j][1]){
                j++;
            }
            else if(firstList[i][1]<secondList[j][1]){
                i++;
            }
            
        }
        return ans;
        
    }

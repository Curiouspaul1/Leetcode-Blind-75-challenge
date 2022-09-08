    vector<int> ans;
    int row = matrix.size();
    int col = matrix[0].size();

    int sR = 0;     // sR = starting Row
    int sC = 0;     // sC = starting column
    int eR = row-1; // eR = ending row
    int eC = col-1; // eC = ending column
    
    int count = 0;
    int total = row*col;
    
    while(count<total)
    {
        for(int index = sC ; count<total && index <= eC ; index++)
        {
            ans.push_back(matrix[sR][index]);
            count++;
        }
        sR++;  // bcoz we need to exclude the element '3' coz its already printed
        
        for(int index = sR ; count<total && index<=eR ; index++)
        {
            ans.push_back(matrix[index][eC]);
            count++;
        }
        eC--; // '9' to be excluded from the list coz already been considered
        
        for(int index = eC ; count<total && index >= sC ; index--)
        {
             ans.push_back(matrix[eR][index]);
            count++;
        }
        eR--;
        
        for(int index = eR ; count<total && index >= sR ; index--)
        {
            ans.push_back(matrix[index][sC]);
            count++;
        }
        sC++;
    }
    return ans;
    
    }
};

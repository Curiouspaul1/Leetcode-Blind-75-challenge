int startWindow = 0, endWindow = 0;
        int size = s.length();
        
        unordered_map<char, int> hash;
        int maxLength = 0;
        
        while(endWindow < size) {
            char currentChar = s[endWindow];
            hash[currentChar]++;
            
            while(endWindow - startWindow + 1 != hash.size()) {
                char startChar = s[startWindow];
                hash[startChar]--;
                
                if (hash[startChar] == 0) hash.erase(startChar);
                startWindow++;
            }
            
            maxLength = max(maxLength, endWindow - startWindow + 1);
            endWindow++;
        }
        
        return maxLength;

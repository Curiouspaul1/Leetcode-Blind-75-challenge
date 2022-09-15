class Solution {
public:
    int characterReplacement(string s, int k) {
        int l = 0;
        std::vector frequencies = std::vector(26, 0);
        
        int max_frequency = 0;
        int result = 0;
        for(int r = 0; r < s.size(); r++){
            frequencies[s[r] - 'A']++;
            max_frequency = *std::max_element(frequencies.begin(), frequencies.end());
            if(r - l + 1  - max_frequency <= k) result = std::max(result, r - l + 1);
            else{
                frequencies[s[l] - 'A']--;
                l++;
            }
        }

        return result; 
    }
};

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ''
        
        def palindrome(j):
            score = ''

            start = j
            stop = j+1
            # print('even')
            while (start >= 0) and (stop < n) and (s[start] == s[stop]):
                score = s[start:stop+1]
                # print(s[start:stop+1])
                start -= 1
                stop += 1

            start = j
            stop = j
            # print('odd')
            while (start >= 0) and (stop < n) and (s[start] == s[stop]):
                if (stop-start+1)>len(score):
                    score = s[start:stop+1]
                # print(s[start:stop+1])
                start-=1
                stop+=1
            # print(score)
            return score
        
        for j in range(n):
            temp = palindrome(j)
            if len(temp) > len(result):
                result = temp
        
        return result

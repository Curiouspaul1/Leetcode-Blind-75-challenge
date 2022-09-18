class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check_substring(index, temp):
            if index==len(s) or s[index] in temp:
                return len(temp)
            return check_substring(index+1, temp+s[index])
        big=0
        for index in range(len(s)):
            big=max(big, check_substring(index, temp=""))
        return big
        
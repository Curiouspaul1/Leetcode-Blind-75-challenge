class Solution:
    def isAnagram(self, s, t):
        return s.sort() == t.sort()

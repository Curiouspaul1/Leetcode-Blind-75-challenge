class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
            if len(s) != len(t):
                return False
            s_dict={}
            t_dict={}
            for letter in s:
                s_dict[letter]=1+s_dict.get(letter, 0)
            
            for letter in t:
                t_dict[letter]=1+t_dict.get(letter, 0)
            
            for letter in s_dict:
                if s_dict[letter] != t_dict.get(letter, 0):
                    return False
                
            # for letter in t_dict:
            #     if letter not in s_dict  or s_dict[letter] != t_dict[letter]:
            #         return False
            return True
                
        
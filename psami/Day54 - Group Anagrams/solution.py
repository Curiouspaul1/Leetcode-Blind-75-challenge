from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        output_list = []
        for i in strs:
            sorted_i = "".join(sorted(i))
            ana_dict[sorted_i] = ana_dict.get(sorted_i, [])

            ana_dict[sorted_i].append(i)

        for x in ana_dict:
            output_list.append(ana_dict[x])
        return output_list


x = Solution()
print(x.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
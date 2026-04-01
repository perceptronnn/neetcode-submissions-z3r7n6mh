class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            char_list = [0] * 26
            for c in s:
                char_list[ord(c) - ord('a')] += 1
            key = tuple(char_list)
            groups.setdefault(key, []).append(s)
        return groups.values() 
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        sortedMap = {}
        for s in strs:
            if str(sorted(s)) in sortedMap:
                sortedMap[str(sorted(s))].append(s)
            else:
                sortedMap[str(sorted(s))] = [s]
        result = []
        for vals in sortedMap.values():
            result.append(vals)
        return result
        
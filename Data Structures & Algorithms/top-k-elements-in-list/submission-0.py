class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {}
        for num in nums:
            #frequencyMap.setdefault(num, 0) += 1
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
        
        frequencyTuples = list(frequencyMap.items())
        
        res = sorted(frequencyTuples, key = lambda x: x[1], reverse=True)
        res = res[0:k]
        ans = []
        for r in res:
            ans.append(r[0])
        return ans
        
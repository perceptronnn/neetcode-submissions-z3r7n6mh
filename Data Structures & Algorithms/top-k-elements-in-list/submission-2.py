class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            freqs[num] = freqs.get(num, 0) + 1
        
        res = [[] for i in range(len(nums))]
        #print(res)
        for p, v in freqs.items():
            res[v - 1].append(p)

        ans = []
        print(freqs)
        print(res)
        for i in range(len(res) - 1, -1, -1):
            print(i)
            for j in res[i]:
                print(".   " + str(j))
                ans.append(j)
                print(ans)
                print("k: " + str(k))
                print("len(ans): " + str(len(ans)))
                if len(ans) == k:
                    print("if")
                    return ans
        return ans
        
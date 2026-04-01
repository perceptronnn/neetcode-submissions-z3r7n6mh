class Solution:
    def trap(self, height: List[int]) -> int:
        l = []
        r = []
        mx = 0
        result = 0
        for h in height:
            if h > mx:
                l.append(0)
                mx = h
            else:
                l.append(mx - h)
        mx = 0
        for h in reversed(height):
            if h > mx:
                r.append(0)
                mx = h
            else:
                r.append(mx - h)
        r = list(reversed(r))
        for i in range(len(height)):
            result += min(l[i], r[i])
        return result 
        
        
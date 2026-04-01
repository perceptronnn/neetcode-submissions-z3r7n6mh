class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1Map, s2Map = self.toMap(s1), self.toMap(s2[:len(s1)])
        m = self.matches(s1Map, s2Map)
        l, r = 0, len(s1) - 1

        while r < len(s2):
            print(m)
            print(s1Map)
            print(s2Map)
            print(l, r)
            print(s2[l], s2[r])
            #if m == len(s1Map):
            if self.isSame(s1Map, s2Map):
                return True
            if s2[l] in s1Map and s1Map[s2[l]] == s2Map[s2[l]]:
                m -= 1    
            s2Map[s2[l]] -= 1
            l += 1
            r += 1
            if r < len(s2):
                if s2[r] in s2Map:
                    s2Map[s2[r]] += 1
                else:
                    s2Map[s2[r]] = 1
                if (s2[r] in s1Map) and (s1Map[s2[r]] == s2Map[s2[r]]):
                    m += 1 
                    print("heeel " + str(m))
        return self.isSame(s1Map, s2Map)

    def toMap(self, s):
        mp = {}
        for c in s:
            if c in mp:
                mp[c] += 1
            else:
                mp[c] = 1
        return mp
    
    def matches(self, s1M, s2M):
        m = 0
        for k in s1M:
            if k in s2M and s1M[k] == s2M[k]:
                m += 1
        return m
    
    def isSame(self, s1M, s2M):
        for k in s1M:
            if k in s2M and s1M[k] == s2M[k]:
                continue
            else:
                return False
        return True
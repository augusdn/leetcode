class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t) > len(s): return ""
        
        tCount, wCount = {}, {}
        for c in t:
            tCount[c] = 1 + tCount.get(c, 0)
            
        have, need = 0, len(tCount)
        res = [-1, -1]
        rLen = float('inf')
        l = 0
        
        for r in range(len(s)):
            c = s[r]
            wCount[c] = 1 + wCount.get(c, 0)
            
            if c in tCount and tCount[c] == wCount[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < rLen:
                    res = [l,r]
                    rLen = (r-l+1)
                wCount[s[l]] -= 1
                if s[l] in tCount and tCount[s[l]] > wCount[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if rLen != float('inf') else ""
                    
            

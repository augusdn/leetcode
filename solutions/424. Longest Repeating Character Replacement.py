class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        l = 0
        mostFrequent = 0
        count = {}
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            mostFrequent = max(mostFrequent, count[s[r]])
            
            if (r-l+1) - mostFrequent > k:
                count[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, r-l+1)
            
        return maxLength

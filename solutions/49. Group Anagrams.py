class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for str in strs:
            s = "".join(sorted(str))
            if s in seen.keys():
                l = seen[s]
                l.append(str)
            else:
                seen[s] = [str]
​
        res = []
        for a in seen:
            res.append(seen[a])
​
        return res

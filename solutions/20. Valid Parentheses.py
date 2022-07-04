class Solution:
    def isValid(self, s: str) -> bool:
        oDict = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in oDict:
                stack.append(c)
                continue
            if not stack or stack[-1] != oDict[c]:
                return False
            stack.pop()
            
        return not stack

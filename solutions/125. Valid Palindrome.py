class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = self.cleanse(s)
        if ns == '':
            return True
        l, r = 0, len(ns) -1
        while l < r:
            print("l: %c r: %c" % (ns[l], ns[r]))
            if ns[l] != ns[r]:
                return False
            l += 1
            r -= 1
        return True
    
    def cleanse(self, s):
        ns = ''.join([i.lower() for i in s if i.isalnum()])
        return ns

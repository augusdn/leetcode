class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        indexQ = deque()
        valQ = deque()
        
        res = []
        for i, n in enumerate(nums):
            # loop thru valQ and remove all values less than n for current Window
            while valQ and n > valQ[-1]:
                valQ.pop()
                indexQ.pop()
            valQ.append(n)
            indexQ.append(i)
            
            # remove all the item our of current window
            while i - indexQ[0] + 1 > k:
                valQ.popleft()
                indexQ.popleft()
            
            # skip append until we reach window size of k
            if i + 1 >= k:
                res.append(valQ[0])
        return res

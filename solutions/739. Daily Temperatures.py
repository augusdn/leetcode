class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        history = []
        
        for i, t in enumerate(temperatures):
            while history and t > history[-1][0]:
                historyT, historyI = history.pop()
                answer[historyI] = (i - historyI)
            history.append([t, i])
        return answer

class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxCount = 0
        boxes = {}
        for i in range(lowLimit, highLimit+1):
            sum = 0
            for d in str(i):
                sum += int(d)
            if sum not in boxes:
                boxes[sum] = 0
            boxes[sum] += 1
            if boxes[sum] > boxCount:
                boxCount = boxes[sum]
        return boxCount

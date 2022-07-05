class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        
        for t in tokens:
            if (t.strip('-')).isnumeric():
                numbers.append(t)
            else:
                a = numbers.pop()
                b = numbers.pop()
                res = eval(b+t+a)
                numbers.append(str(int(res)))
        return numbers.pop()

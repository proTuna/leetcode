class Solution:
    def addDigits(self, num: int) -> int:
        
        def make(num):
            l = list(str(num))
            ans = [int(i) for i in l]
            return sum(ans)
        while num>9:
            num = make(num)
        return num
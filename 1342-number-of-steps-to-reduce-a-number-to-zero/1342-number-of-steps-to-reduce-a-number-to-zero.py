class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        cnt = 0
        while num:
            num = num//2 if num%2==0 else num-1
            cnt+=1
            
        return cnt
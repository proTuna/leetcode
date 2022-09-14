class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = {5:0,10:0,20:0}
        for bill in bills:
            if bill == 10:
                if c[5] == 0:
                    return False
                else:
                    c[5]-=1
            elif bill == 20:
                if c[10] != 0 and c[5] != 0:
                    c[10] -=1
                    c[5] -= 1
                elif c[5] >=3:
                    c[5] -=3
                else:
                    return False
            c[bill]+=1
        return True
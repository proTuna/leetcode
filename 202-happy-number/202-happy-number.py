class Solution:
    def isHappy(self, n: int) -> bool:
        # 2 -> 4 / 4 -> 16 / 37 -> 9+49 / 58 -> 25+64 / 89 -> 64 +81 / 145 -> 1+16+25 / 42 -> 16+4 -> 20 / 4
        ans = True
        c = []
        c.append(n)
        while n!=1:
            s = 0
            while True:
                q = n//10
                r = n%10
                s += r**2
                n = q
                if q==0:
                    break
            if s in c:
                return False
            else:
                c.append(s)
                n = s
        return ans
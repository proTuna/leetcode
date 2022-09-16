class Solution:
    def maximum69Number (self, num: int) -> int:
        ans = num
        l = []
        while num:
            q = num//10
            r = num%10
            l.append(r)
            num = q
        l.reverse()
        for i in range(len(l)):
            tmp = 0
            if l[i] == 6:
                l[i] = 9
                tmp = int(''.join(map(str,l)))
                l[i] = 6
            else:
                l[i]= 6
                tmp = int(''.join(map(str,l)))
                l[i] = 9
            ans = max(ans,tmp)
        
        return ans
class Solution:
    def mySqrt(self, x: int) -> int:
        n = 0.5*(1+(x/1))
        tmp = 0
        while True:
            tmp = n
            n = 0.5*(n+(x/n))
            if tmp-n<0.005 or tmp-n<-0.005:
                break
        return int(n)

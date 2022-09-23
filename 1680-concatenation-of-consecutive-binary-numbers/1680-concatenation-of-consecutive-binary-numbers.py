class Solution:
    def concatenatedBinary(self, n: int) -> int:
        x = ''
        for i in range(1,n+1):
            x+= "{0:b}".format(i)
        return int(x,2)%1000000007
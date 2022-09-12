class Solution:
    def integerReplacement(self, n: int) -> int:
        # 모든 홀수는 4로 나누면 나머지가 1 아니면 3이다. 나머지가 1이면 n에서 1을 빼고 3이면 n에서 1을 더하는 게 더 효율적이다.
        cnt = 0
        while n != 1:
            if n%2 == 0:
                n //= 2
            elif n%4 == 1 or n == 3:
                n-=1
            else:
                n+=1
            cnt+=1
        return cnt
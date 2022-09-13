import heapq as hq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        hq1 = [[-i,j] for i,j in zip(profits,capital)]
        hq2 = []
        hq.heapify(hq1)
        
        while hq1 and k:
            i,j = hq.heappop(hq1)
            if j <= w:
                w += -i
                k -=1
            else:
                hq.heappush(hq2,[j,i])
            while hq2 and hq2[0][0] <= w:
                j,i = hq.heappop(hq2)
                hq.heappush(hq1,[i,j])
        return w
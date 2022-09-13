class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : (x[1],x[0]))
        l = len(intervals)
        ans = 0
        last = -int(1e9)
        for i in range(l):
            if intervals[i][0] < last:
                ans +=1
            else:
                last = intervals[i][1]
                
        return ans
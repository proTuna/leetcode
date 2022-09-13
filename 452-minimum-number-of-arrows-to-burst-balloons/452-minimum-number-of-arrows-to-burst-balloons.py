class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 풍선을 터트리기 위한 최소 화살표 수
        points.sort(key=lambda x: (x[1],x[0]))
        ans = 0
        last = -float('inf')
        l = len(points)
        for i in range(l):
            if points[i][0] <= last:
                continue
            else:
                last = points[i][1]
                ans+=1
        return ans
import heapq as hq

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = [(speed[i],efficiency[i]) for i in range(n)]
        engineers.sort(key=lambda x: -x[1])
        a = []
        total_speed = 0
        performance = 0
        for s,e in engineers:
            hq.heappush(a,s)
            total_speed += s
            if len(a) > k:
                total_speed -= hq.heappop(a)
            performance = max(performance, total_speed*e)
        return performance%1000000007
import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = int(1e9)
        graph = [[] for _ in range(101)]
        distance = collections.defaultdict(int)
        
        for time in times:
            a,b,c = time
            graph[a].append((b,c))
        
        q = []
        hq.heappush(q,(0,k))
        while q:
            dist, now = hq.heappop(q)
            if now not in distance:
                distance[now] = dist
                for v,w in graph[now]:
                    cost = dist + w
                    hq.heappush(q,(cost,v))
                    
        if len(distance) == n:
            return max(distance.values())
        return -1
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = [[] for _ in range(numCourses)]
        
        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] +=1
        result = []
        q = collections.deque()
            
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        while q:
            now = q.popleft()
            result.append(now)
            for i in graph[now]:
                indegree[i] -=1
                if indegree[i] == 0:
                    q.append(i)
        return False if sum(indegree) else True
                
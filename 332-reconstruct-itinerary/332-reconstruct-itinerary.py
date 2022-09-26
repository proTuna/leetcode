class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        ans = []
        for a,b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            ans.append(a)
            
        dfs('JFK')
        return ans[::-1]
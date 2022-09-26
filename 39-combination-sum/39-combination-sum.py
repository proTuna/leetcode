class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        def dfs(csum,index,path):
            if csum < 0:
                return
            if csum == 0:
                answer.append(path)
                return
            for i in range(index,len(candidates)):
                dfs(csum-candidates[i],i,path + [candidates[i]])
                
        dfs(target,0,[])
        return answer
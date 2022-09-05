class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a = []
        
        for weaker in range(len(mat)):
            pair = (mat[weaker].count(1),weaker)
            a.append(pair)
        
        a.sort(key = lambda x: x[0])
        
        ans = [j for (i,j) in a]
        return ans[:k]
            
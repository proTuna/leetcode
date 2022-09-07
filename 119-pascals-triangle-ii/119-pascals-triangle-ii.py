class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]*i for i in range(1,35)]
        for i in range(2,34):
            for j in range(len(ans[i])):
                if j == 0 or j == len(ans[i])-1:
                    continue
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans[rowIndex]
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        l = len(strs)

        if strs[0] == "":
            return ans
        else:
            flag = True
            for i in strs[0]:
                ans+=i
                for j in range(1,l):
                    if not strs[j].startswith(ans):
                        flag = False
                        break
                if not flag:
                    ans = ans[:-1]
        return ans
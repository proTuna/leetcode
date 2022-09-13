class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = {}
        words = s.split()
        if len(pattern) != len(words) or len(set(pattern)) != len(set(words)):
            return False
        for i,v in enumerate(pattern):
            if v in p: # v와 단어를 매칭시킨다.
                if p[v] != words[i]:
                    return False
            else:
                p[v] = words[i]
        return True
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_occ= {}
        
        for i in range(len(s)):
            last_occ[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in stack:
                # 스택이 비어있지 않고,
                # 스택의 top이 현재 넣으려는 값보다 크며,
                # 스택의 top이 미래에 다시 사용될 것이라면 
                # 스택에서 pop을 한다.
                while (stack and stack[-1] >= s[i] and last_occ[stack[-1]] >= i):
                    stack.pop()
                stack.append(s[i])
        
        return ''.join(stack)
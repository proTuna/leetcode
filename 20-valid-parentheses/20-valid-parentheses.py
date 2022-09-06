class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = { ")":"(", "]":"[", "}":"{" }
        
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
            else:
                if len(stack)>0 and stack[-1] == parentheses[i]:
                    stack.pop()
                else:
                    stack.append(i)
                    
        if len(stack) == 0:
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join([i.lower() for i in s if i.isalpha() or i.isnumeric()])
        return text == text[::-1]
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        braces = {'(': ')', '{': '}', '[': ']'}

        for c in s:
            if c in braces.keys():
                stack.append(c)
            elif len(stack) == 0 or braces[stack.pop()] != c:
                return False

        return len(stack) == 0
        
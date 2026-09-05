class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        clostToOpen = {")":"(", "}":"{", "]":"["}

        for c in s:
            if c in clostToOpen:
                if stack and clostToOpen.get(c) == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
        
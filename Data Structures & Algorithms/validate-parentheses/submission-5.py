class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')': '(', '}': '{', ']': '['}
        stack = []
        for letter in s:
            if letter in chars:
                if len(stack) == 0:
                    return False
                if stack.pop() == chars[letter]:
                    continue
                else:
                    return False
            stack.append(letter)
        return len(stack) == 0
                
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        max_length = 0
        seen = {}  
        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= start:
                start = seen[letter] + 1
            seen[letter] = i
            max_length = max(max_length, i - start + 1)
        return max_length
                 
            

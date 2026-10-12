class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        max_length = 0
        l = 0
        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= l:
                l = seen[letter] + 1
                seen[letter] = i
            seen[letter] = i
            max_length = max(max_length, i - l + 1)
        return max_length
        
            
            
            
            
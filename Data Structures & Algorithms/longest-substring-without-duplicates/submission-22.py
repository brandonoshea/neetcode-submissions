class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        max_length = 0
        seen = {}
        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            seen[char] = r
            max_length = max(r - l + 1, max_length)
        return max_length

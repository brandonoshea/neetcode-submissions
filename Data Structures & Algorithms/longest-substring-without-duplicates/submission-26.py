class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        l = 0
        duplicates = {}
        for r in range(len(s)):
            if s[r] in duplicates and duplicates[s[r]] >= l:
                l = duplicates[s[r]] + 1

            duplicates[s[r]] = r
            max_length = max(max_length, r - l + 1)

        return max_length





            
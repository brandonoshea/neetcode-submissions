class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        max_length = 0

        for i, letter in enumerate(s):
            while letter in seen:
                seen.remove(s[start])
                start += 1
            seen.add(letter)
            max_length = max(max_length, i - start + 1)
        return max_length
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        counts = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for key, count in count.items():
            counts[count].append(key)
        result = []
        for n in range(len(counts) - 1, 0, -1):
            for word in counts[n]:
                result.append(word)
                if len(result) == k:
                    return result


from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for n, c in count.items():
            arr[c].append(n)
        result = []
        for i in range(len(arr) -1 , 0, -1):
            for n in arr[i]:
                result.append(n)
                if len(result) == k:
                    return result



            
            
            
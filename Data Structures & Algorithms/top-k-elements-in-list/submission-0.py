class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        all_items = list(num_freq.items())

        sorted_items = sorted(all_items, key=lambda x: x[1], reverse = True)
        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]
        
        ## Solution 1 with time complexity O(nlogn)
        frequency_map = defaultdict(int)
        for num in nums:
            frequency_map[num] += 1
        sorted_list = sorted(frequency_map.keys(), 
                        key=lambda x: frequency_map[x], 
                        reverse=True)
        return sorted_list[:k]

        ## Solution 2 with Time complexity O(n)
        """ 
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range (len(freq)-1 , 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res 
        """

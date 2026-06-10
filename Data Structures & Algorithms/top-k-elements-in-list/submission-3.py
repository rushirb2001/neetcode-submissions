import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) 
        print(count)
        """
        Inbuilt function from collections to created a counted 
        """
        return [num for num, freq in 
                heapq.nlargest(k, count.items(), key=lambda x:x[1])]

        # # return [num for num, freq in 
        #         # sorted(count.items(), key=lambda x: x[1], 
        #             # reverse=True)[:k]]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        my_hash = defaultdict(int)

        for i in nums:
            my_hash[i] += 1
        
        sorted_dict = dict(sorted(my_hash.items(),key =lambda x:x[1], reverse=True))


        result = list(sorted_dict.keys())[:k]
        return(result)
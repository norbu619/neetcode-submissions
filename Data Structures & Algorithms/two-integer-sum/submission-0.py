class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        my_hash = {}

        for i in range(len(nums)):
            if nums[i] in my_hash:
               return [my_hash[nums[i]], i]
            
            t = target - nums[i]
            my_hash[t] = i
            
        
                
        
        return


        
        
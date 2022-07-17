class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Approach - 1
	# for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
                
                
	# Approach - 2 
        dic = {}
        for index, num in enumerate(nums):
            remain = target - num
            if remain in dic:
                return [dic[remain], index]
            dic[num] = index
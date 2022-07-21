class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        check = 0
        if not nums: return 0
        for i in nums:
            if nums[check] != i:
                check += 1
                nums[check] = i
        return check + 1

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach -> 1
        check = 0
        for i in range(len(nums)):
            if nums[check] != val:
                check += 1
            elif nums[check] == val and nums[i] != val:
                nums[check], nums[i] = nums[i], nums[check]
                check += 1
            else:
                continue
        return check

        # Approach - 2
        # i = 0
        # for j in range(len(nums)):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i+=1
        # return i
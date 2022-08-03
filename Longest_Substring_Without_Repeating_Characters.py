class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_list = []
        length = 0
        for i in s:
            while i in temp_list:
                temp_list.pop(0)
            temp_list.append(i)
            length = max(length,len(temp_list))
        return length

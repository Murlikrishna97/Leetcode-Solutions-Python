class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                temp = haystack[i:i+len(needle)] == needle[0:len(needle)]
                if temp:
                    return i
        return -1
        
        #Using Python Built-in Function
        
        #return haystack.find(needle)        

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
    	# Approach - 1
        # new_str = ""
        # if len(strs) == 0: return new_str
        # sorts = sorted(strs, key=len)
        # short_word = min(sorts, key=len)
        # for j in range(len(short_word)):
        #     for i in range(1, len(sorts)):
        #         if sorts[0][j] != sorts[i][j]:
        #             return new_str
        #     new_str = new_str + sorts[0][j]
        # return new_str
        
        # Approach - 2 --> Faster
        new_str = ""
        if len(strs) == 0:
            return new_str
        elif len(strs) == 1:
            return strs[0]
        else:
            try:
                for j in range(len(strs[0])):
                    for i in range(1, len(strs)):
                        if strs[0][j] != strs[i][j]:
                            return new_str
                    new_str = new_str + strs[0][j]
                return new_str
            except:
                return new_str



#IGNORE BELOW THIS LINE
##########################################################
        #
        # ans = ''
        # for i,val in enumerate(zip(*strs)):
        #     if len(set(val)) == 1:
        #         ans+= val[0]
        #     else:
        #         break
        # return ans

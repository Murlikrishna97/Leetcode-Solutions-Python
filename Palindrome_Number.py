class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Approach - 1
#       str_x = str(x)
#       list = "".join(reversed(str_x))
#       string = "".join(list)
#       if str_x == string:
#             return True
#         return False

        # Approach - 2
        return str(x) == str(x)[::-1]
        
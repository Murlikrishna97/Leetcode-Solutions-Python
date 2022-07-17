class Solution:
    def romanToInt(self, s: str) -> int:
        # Approach - 1 
        
        # num = 0
        # for i in range(len(s)):
        #     if s[i] == 'I':
        #         num = num + 1
        #     elif s[i] == 'V':
        #         if s[i-1] == 'I' and i != 0:
        #             num = num + 3
        #         else:
        #             num = num + 5
        #     elif s[i] == 'X':
        #         if s[i-1] == 'I' and i != 0:
        #             num = num + 8
        #         else:
        #             num = num + 10
        #     elif s[i] == 'L':
        #         if s[i-1] == 'X' and i != 0:
        #             num = num + 30
        #         else:
        #             num = num + 50
        #     elif s[i] == 'C':
        #         if s[i-1] == 'X' and i != 0:
        #             num = num + 80
        #         else:
        #             num = num + 100
        #     elif s[i] == 'D':
        #         if s[i-1] == 'C' and i != 0:
        #             num = num + 300
        #         else:
        #             num = num + 500
        #     elif s[i] == 'M':
        #         if s[i-1] == 'C' and i != 0:
        #             num = num + 800
        #         else:
        #             num = num + 1000
        #     else:
        #         pass
        # return num
        
        # Approach - 2
        rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if s[i - 1] in rom_dict.keys():
                if s[i-1] == 'I' and s[i] == 'V' and i != 0:
                    num = num + 3
                elif s[i-1] == 'I' and s[i] == 'X' and i != 0:
                    num = num + 8
                elif s[i-1] == 'X' and s[i] == 'L' and i != 0:
                    num = num + 30
                elif s[i-1] == 'X' and s[i] == 'C' and i != 0:
                    num = num + 80
                elif s[i-1] == 'C' and s[i] == 'D' and i != 0:
                    num = num + 300
                elif s[i-1] == 'C' and s[i] == 'M' and i != 0:
                    num = num + 800
                else:
                    num = num + rom_dict[s[i]]
        return num

class Solution:
    def isValid(self, s: str) -> bool:
        valid_list = []
        for i in s:
            if i == ')':
                if not valid_list or '(' not in valid_list: return False
                if valid_list[-1] == '(': valid_list.pop()
            elif i == ']':
                if not valid_list or '[' not in valid_list: return False
                if valid_list[-1] == '[': valid_list.pop()
            elif i == '}':
                if not valid_list or '{' not in valid_list: return False
                if valid_list[-1] == '{': valid_list.pop()
            else:
                valid_list.append(i)

        return not valid_list
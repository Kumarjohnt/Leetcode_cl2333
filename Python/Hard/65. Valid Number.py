class Solution:
    def isNumber(self, s: str) -> bool:
        has_number, has_dot, has_e = False, False, False
        for i, c in enumerate(s):
            if c in "+-":
                if i > 0 and s[i - 1] not in 'eE':
                    return False
            elif c == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif c in 'eE':
                if has_e or not has_number:
                    return False
                has_e, has_number = True, False
            elif c.isdigit():
                has_number = True
            else:
                return False
        return has_number
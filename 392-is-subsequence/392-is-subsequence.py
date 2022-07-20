class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (s == t):
            return True
        else:
            result = ''
            s_index = 0
            for t_index in range(len(t)):
                if (s_index < len(s)):
                    if (s != '' and s[s_index] == t[t_index]):
                        result += t[t_index]
                        s_index += 1
            if (result == s):
                return True
            else:
                return False

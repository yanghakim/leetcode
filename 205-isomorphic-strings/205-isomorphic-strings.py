class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = {}
        mapping_t_s = {}
        
        for (s1, t1) in zip(s, t):
            
            if (s1 not in mapping_s_t) and (t1 not in mapping_t_s):
                mapping_s_t[s1] = t1
                mapping_t_s[t1] = s1
            elif mapping_s_t.get(s1) != t1 or mapping_t_s.get(t1) != s1:
                return False
        return True
                
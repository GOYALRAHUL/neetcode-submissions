class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringone={}
        stringtwo={}
        if len(s) != len(t):
            return False
        else:
            for st1 in s:
                stringone[st1] = stringone.get(st1, 0) + 1
            for st2 in t:
                stringtwo[st2] = stringtwo.get(st2, 0) + 1
            for key in stringone:
                if stringone.get(key) != stringtwo.get(key):
                    return False
        return True
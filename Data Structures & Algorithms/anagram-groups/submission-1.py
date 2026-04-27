class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for strng in strs:
            count=[0]*26
            for c in strng:
                count[ord(c)-ord('a')] +=1
            res[tuple(count)].append(strng)
        return list(res.values())


      



        
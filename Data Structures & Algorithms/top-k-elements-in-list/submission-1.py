class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct=dict()
        tmplst=[[] for i in range(len(nums)+1)]
        for n in nums:
            dct[n]= dct.get(n,0)+1
        for key,value in dct.items():
           tmplst[value].append(key)
           res=[]
        for i in range(len(tmplst)-1,0,-1):
            for n in tmplst[i]:
                res.append(n)
                if len(res)==k:
                    return res

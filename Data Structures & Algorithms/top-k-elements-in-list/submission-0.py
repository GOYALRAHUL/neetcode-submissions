class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct=dict()
        tmplst=[]
        for n in nums:
            dct[n]= dct.get(n,0)+1
        for key,value in dct.items():
            tmplst.append([value,key])
        tmplst.sort(reverse=True)
        finlst=[]
        for lst in tmplst[0:k]:
            finlst.append(lst[1])
        return finlst
        
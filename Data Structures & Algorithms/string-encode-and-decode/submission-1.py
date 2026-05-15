class Solution:

    def encode(self, strs: List[str]) -> str:
        enc=""
        for s in strs:
            enc=enc+str(len(s))+"#"+s
        print(f"encode{enc}")
        return enc


    def decode(self, s: str) -> List[str]:
        initlen=""
        i=0
        finallst=[]
        while i < len(s):
            if s[i] !='#':
                initlen = initlen+s[i]
                i+=1
            elif s[i] == '#':
                finallst.append(s[i+1:i+int(initlen)+1])
                i=i+int(initlen)+1
                initlen=""
            
        return finallst




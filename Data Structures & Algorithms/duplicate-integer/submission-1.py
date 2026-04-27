class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_num=[]
        for num in nums:
            if num in temp_num:
                return True
            temp_num.append(num)
        return False
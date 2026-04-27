class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_num=set()
        for num in nums:
            if num in temp_num:
                return True
            temp_num.add(num)
        return False
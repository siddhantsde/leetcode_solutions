class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        num1 = []

        for i in nums:
            if i != val:
                num1.append(i)
        
        cnt = len(num1)

        for i in range(0,cnt):
            nums[i] = num1[i]
        for i in range(cnt, len(nums)):
            nums[i] = val
        return cnt
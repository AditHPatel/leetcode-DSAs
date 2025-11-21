class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        lsubset = set()
        lpt = 0
        cTotal = 0
        total = 0

        for rpt in range(len(nums)): 
            while nums[rpt] in lsubset:
                lsubset.remove(nums[lpt])
                cTotal -= nums[lpt]
                lpt += 1


            lsubset.add(nums[rpt])
            cTotal += nums[rpt]
            total = max(total, cTotal)
        
        return total


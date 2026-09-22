class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums = set(nums)
        nums = sorted(nums)

        if not nums:
            return 0

        c = 1
        best = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                c += 1
                best = max(c, best)
            else:
                c = 1

        return best
        
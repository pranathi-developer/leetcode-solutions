class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]

        total = prefix[n - 1]

        for i in range(n):
            left = prefix[i] - nums[i]
            right = total - prefix[i]

            if left == right:
                return i

        return -1
        
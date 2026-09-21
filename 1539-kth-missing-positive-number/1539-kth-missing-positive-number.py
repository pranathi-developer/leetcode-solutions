class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1

        while k > 0:
            if num not in arr:
                k -= 1
            num += 1

        return num - 1
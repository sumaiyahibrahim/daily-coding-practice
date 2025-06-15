class Solution(object):
    def minimizeMax(self, nums, p):
        if p == 0:
            return 0
        nums.sort()
        n, left, right = len(nums), 0, nums[-1] - nums[0]
        while left < right:
            mid, pairs = left + (right - left) // 2, 0
            i = 1
            while i < n:
                if nums[i] - nums[i-1] <= mid:
                    pairs += 1
                    i += 1
                i += 1
            if pairs >= p:
                right = mid
            else:
                left = mid + 1
        return left

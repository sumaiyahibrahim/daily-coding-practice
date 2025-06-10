class Solution:
    def maxDifference(self, s):
        mpp = [0] * 26
        maxi = 0
        mini = len(s)
        for c in s:
            mpp[ord(c) - ord('a')] += 1
        for i in range(26):
            if mpp[i] % 2 != 0:
                maxi = max(maxi, mpp[i])
            if mpp[i] % 2 == 0 and mpp[i] > 0:
                mini = min(mini, mpp[i])
        return maxi - mini

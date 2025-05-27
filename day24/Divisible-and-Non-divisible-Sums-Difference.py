class Solution(object):
    def differenceOfSums(self, n, m):
        totalSum = n * (n + 1) // 2
        divisibleSum = m * (n // m) * (n // m + 1) 
        return totalSum - divisibleSum

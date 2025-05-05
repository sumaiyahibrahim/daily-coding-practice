class Solution(object):
    def numTilings(self, n):
        mod = int(1e9 + 7)
        
        def dominoes(i, n, possible): 
            if i == n:
                return 0 if possible else 1
            if i > n:
                return 0
            if possible:
                return (dominoes(i + 1, n, False) + dominoes(i + 1, n, True)) % mod
            return (dominoes(i + 1, n, False) + dominoes(i + 2, n, False) + 2 * dominoes(i + 2, n, True)) % mod
        
        return dominoes(0, n, False)
 

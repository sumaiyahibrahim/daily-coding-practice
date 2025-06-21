class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)

        def greedy(minF):
            rm = 0
            for x in freq.values():
                if x < minF:
                    rm += x
                elif x > minF + k:
                    rm += x - minF - k
            return rm

        ans = len(word)
        for minF in freq.values():
            ans = min(ans, greedy(minF))
        return ans

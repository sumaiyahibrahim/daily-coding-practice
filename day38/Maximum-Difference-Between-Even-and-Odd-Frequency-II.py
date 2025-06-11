class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')

        # Step 1: Try all (a, b) pairs
        for a in range(5):
            for b in range(5):
                if a == b: continue

                s1 = [0] * (n + 1)
                s2 = [0] * (n + 1)

                # Step 2: Prefix counts
                for i in range(1, n + 1):
                    s1[i] = s1[i - 1] + (int(s[i - 1]) == a)
                    s2[i] = s2[i - 1] + (int(s[i - 1]) == b)

                # Step 3: Track best past difference for each parity
                g = [[float('-inf')] * 2 for _ in range(2)]
                j = 0

                # Step 4: Two-pointer sliding window
                for i in range(k, n + 1):
                    while i - j >= k and s1[i] > s1[j] and s2[i] > s2[j]:
                        pa = s1[j] % 2
                        pb = s2[j] % 2
                        g[pa][pb] = max(g[pa][pb], s2[j] - s1[j])
                        j += 1

                    # Step 5: Check candidate answer
                    pa = s1[i] % 2
                    pb = s2[i] % 2
                    best = g[1 - pa][pb]
                    if best != float('-inf'):
                        ans = max(ans, (s1[i] - s2[i]) + best)

        return -1 if ans == float('-inf') else ans

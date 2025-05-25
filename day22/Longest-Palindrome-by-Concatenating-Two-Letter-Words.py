class Solution(object):
    def longestPalindrome(self, words):
        mpp = Counter(words)
        count = 0
        alreadyPalindrome = 0
        for w, freq in mpp.items():
            s = w[::-1]
            if w == s:
                count += (freq // 2) * 4
                if freq % 2:
                    alreadyPalindrome = 1
            elif w < s and s in mpp:
                count += min(freq, mpp[s]) * 4
        return count + alreadyPalindrome * 2

class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        res = ""
        length = len(word) - numFriends + 1
        for i in range(0, len(word)):
            temp = word[i : i + length]
            if temp > res:
                res = temp
        return res

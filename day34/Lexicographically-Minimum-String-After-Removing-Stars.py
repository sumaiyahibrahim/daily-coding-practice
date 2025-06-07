class Solution(object):
    def clearStars(self, s):
        heap = []
        deleted = set()
        for i, c in enumerate(s):
            if c == '*':
                ch, neg = heapq.heappop(heap)
                deleted.add(-neg)
            else:
                heapq.heappush(heap, (c, -i))
        res = []
        for i, c in enumerate(s):
            if i in deleted or c == '*': continue
            res.append(c)
        return ''.join(res)

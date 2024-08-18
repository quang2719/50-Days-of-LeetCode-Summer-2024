class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        cache = {}
        def do(i):
            nonlocal cache
            if i==len(books): return 0
            if i in cache: return cache[i]
            
            cur_width = shelfWidth
            max_height = 0
            res = float('inf')
            for j in range(i, len(books)):
                w,h = books[j]
                if cur_width < w:
                    break
                cur_width -= w
                max_height = max(max_height,h)
                res = min(
                    #j in current row
                    res, 
                    #or j will be next element of next row
                    do(j+1) + max_height 
                    )
            cache[i] = res
            return res
        return do(0)
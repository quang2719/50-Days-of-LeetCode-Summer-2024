class Solution:
    class file:
        def __init__(self, x):
            self.val = x
            self.sub = None
            self.par = None
    def minOperations(self, logs: List[str]) -> int:
        head = self.file(0)
        for o in logs:
            if o =='../':
                if head.val == 0: continue
                else: head = head.par
            elif o =='./': continue
            else: #
                new_file = self.file(head.val + 1)
                new_file.par = head
                head.sub = new_file
                head = head.sub
        return head.val
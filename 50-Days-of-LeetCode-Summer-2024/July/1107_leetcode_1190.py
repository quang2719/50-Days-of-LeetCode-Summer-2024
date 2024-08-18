class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            x = s[i]
            if x=='(':
                stack.append(i)
            elif x==')':
                id = stack.pop()
                if id ==0 and i == len(s)-1:
                    s = s[id+1:i][::-1]
                else:
                    s = s[:id] + s[id+1:i][::-1] +s[i+1:]
                    i-=2
            i+=1
        return s
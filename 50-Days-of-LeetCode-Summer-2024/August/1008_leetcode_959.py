class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        roots = {}
        #union find
        def find(x):
            if x not in roots:
                roots[x] = x
            while (x != roots[x]):
                x = roots[x]
            return x
        def union(x, y):
            roots[find(x)] = find(y)
        length = len(grid)
        for i in range(length):
            for j in range(length): 
                #check if the character is '/'
                if grid[i][j] == '/':
                    union((i, j, 'N'), (i, j, 'W'))
                    union((i, j, 'S'), (i, j, 'E'))
                #check if the character is '\'
                elif grid[i][j] == '\\':
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                #check if the character is ' '
                elif grid[i][j] == ' ':
                    union((i, j, 'N'), (i, j, 'E'))
                    union((i, j, 'S'), (i, j, 'W'))
                    union((i, j, 'N'), (i, j, 'W'))    
                #check horizontally adjacent squares,
                #union the E from the left square with W from the right square
                if j > 0:
                    union((i, j-1, 'E'), (i, j, 'W'))
                #check vertcally adjacent squares,
                #union the S from the top square with N from the bottom square
                if i > 0:
                    union((i-1, j, 'S'), (i, j, 'N'))    
        return len(set(map(find, roots)))
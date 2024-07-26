class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(matrix)):
            min_ele_id = matrix[i].index(min(matrix[i]))
            check = True
            for j in range(len(matrix)):
                if matrix[i][min_ele_id] < matrix[j][min_ele_id]:
                    check = False 
                    break
            if check: res.append(matrix[i][min_ele_id])
        return res
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def count_increase_arr(arr):
            max_count = 0
            for i,x in enumerate(arr):
                # i will be the middle element
                count_left = sum([1 for y in arr[:i] if y < x])
                count_right = sum([1 for y in arr[i:] if y > x])
                max_count += (count_left*count_right)
            return max_count
        return (count_increase_arr(rating) + count_increase_arr(rating[::-1]))
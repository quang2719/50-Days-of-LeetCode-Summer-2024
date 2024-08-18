
class Solution:
    """
    Solution class for the LeetCode problem 2134 - Minimum Swaps to Arrange a Binary Grid
    """

    def minSwaps(self, nums: List[int]) -> int:
        # Count the total number of 1's in t
        count_ones = sum(nums)

        # Initialize the window sum to the sum of the first count_ones elements
        window_sum = sum(nums[:count_ones])

        # Initialize the minimum number of swaps to the difference between count_ones and window_sum
        min_swaps = count_ones - window_sum

        # Initialize the window start and end indices
        window_start = 0
        window_end = count_ones - 1

        # Iterate through the remaining elements of the grid
        for i in range(count_ones, len(nums)):

            # Move the window start index forward if the corresponding element is 0
            window_start += 1 if nums[window_start] == 0 else 0

            # Move the window end index forward if the corresponding element is 1
            window_end += 1 if nums[window_end] == 1 else 0

            # Update the window sum by subtracting 1 if the corresponding element is 0
            # and adding 1 if the corresponding element is 1
            window_sum += (0 if nums[window_end] == 1 else -1)
            window_sum += (1 if nums[window_start] == 1 else 0)

            # Update the minimum swaps if the current window sum is less than the minimum swaps
            min_swaps = min(min_swaps, count_ones - window_sum)

        # Return the minimum number of swaps
        return min_swaps



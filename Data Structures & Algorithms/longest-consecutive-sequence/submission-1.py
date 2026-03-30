class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        
        longest_streak = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            # Skip duplicates
            if nums[i] == nums[i-1]:
                continue
            
            # If consecutive, grow the current streak
            if nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                # Streak broken! Save the max and reset
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
        
        # Final check to see if the last streak was the longest
        return max(longest_streak, current_streak)
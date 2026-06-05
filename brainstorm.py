def findConsecutiveOnes(nums: List[int]) -> int:
    max_streak = 0
    current_streak = 0

    for n in nums:
        if n == 1:
            current_streak+=1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0
            
    return max_streak


print(findConsecutiveOnes([1,1,1,0,1,1,1,1]))


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for n in nums:
            if nums[n] = 1:
                current_streak+=1
                max_streak = max(current_streak, max_streak)

            else:
             current_streak = 0        
        return max_streak
            
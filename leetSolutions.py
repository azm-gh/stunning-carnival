
from operator import concat
from typing import List




class Concatenate:
    @classmethod
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) > 1000:
            raise ValueError("nums must incude fewer than 1000 elements")
        
        for num in nums:
            if num < 1 or num > 1000:
                raise ValueError("elements in nums must be between 1 and 1000")
            return nums + nums
    


def shuffle(nums: List[int], n: int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

def shuffle(nums: List[int], n:int) -> List[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[i+n])
    return res

def reverseString(s):
    if not s:
        return s  # Safe guard for empty strings
        
    s = list(s)
    max_idx = len(s) - 1
    
    # Using // ensures we get an integer for the range
    for i in range(len(s) // 2):
        t = s[i]
        s[i] = s[max_idx - i]
        s[max_idx - i] = t
        
    return ''.join(s)


# https://stackoverflow.com/questions/931092/how-do-i-reverse-a-string-in-python
def reverseString2(a_string):
    new_string =''
    index = len(a_string)
    while index:
        index = index -1
        new_string = new_string + a_string[index]
    return new_string


# ELEMENTS vs INDICIES
# If I want the ELEMENTS directly, I use singular noun:
nums = [1,2,3]
for num in nums:
    if num == 1:
        pass

# If yu want INDEX POSITIONS, use i
for i in range(len(nums)):
    if nums[i] == 1:
        pass 


# Sum two numbers in the list based on target
def twoSum(nums: List[int], target: int) -> list[int]:
    for i in range(len(nums)):
        # Inner loop checks every number AFTER the first number
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


def twoSum1(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]
            

twoSum1
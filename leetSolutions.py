
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




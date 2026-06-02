
from operator import concat
from typing import List


concatenated = concat('Hello, ', 'world!')

print(concatenated)


class Solution3:

    @staticmethod 
    def getConcatenation( nums: List[int]) -> List[int]:
        if len(nums) > 1000:
            raise ValueError("nums must include fewer than 1000 elements")
        
        for num in nums:
            if(num < 1 or num > 1000):
                raise ValueError("elements in nums must be between 1 and 1000")
        
        return nums + nums


class Solution4:

    @classmethod
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) > 1000:
            raise ValueError("nums must incude fewer than 1000 elements")
        
        for num in nums:
            if num < 1 or num > 1000:
                raise ValueError("elements in nums must be between 1 and 1000")
            


class Solution5:
    @staticmethod
    def getConcatenation(nums: List[int]) -> List[int]:
        if len(nums) > 1000:
            raise ValueError("nums size must be less than or equal 1000")
        
        for num in nums:
            if num < 0 or num > 1000:
                raise ValueError("elements in nums must be between 1 and 1000")
            
        
        return nums + nums
    

print(Solution5.getConcatenation([1,2,3]))


#example of class method - it passes first 
class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name: str):
        first, last = full_name.split(" ")
        return cls(first, last)
    
    def __str__(self) -> str:
        return f"User: {self.first_name} {self.last_name}"


user1 = User("Jakub", "Jehlik")
user2 = User.from_full_name("Jane Smith")
print(user1)
print(user2)

# single linked list

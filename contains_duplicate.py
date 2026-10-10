# Given an integer array nums, 
# return true if any value appears at least twice in the array, and 
# return false if every element is distinct.

"""
Input: nums = [1,2,3,1]
Output: true
Explanation: The value 1 appears twice in the array.

Input: nums = [1,2,3,4]
Output: false
Explanation: All elements are distinct.

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
Explanation: The values 1, 2, 3, and 4 all appear multiple times.
"""

"""
using a set to add numbers to and compare the lengths of the original array and set
if they are not equal, that means there are duplicates within the original array
"""


def contains_duplicate(nums: list[int]) -> bool:

  check = set()

  for n in nums:
    if n in check:
      return True
    check.add(n)

  return len(nums) != len(check)


assert(contains_duplicate([1,2,3,1]) == True)
assert(contains_duplicate([1,2,3,4]) == False)
assert(contains_duplicate([1,1,1,3,3,4,3,2,4,2]) == True)
assert(contains_duplicate([1,1]) == True)

# O(n) time -> iterating through length of nums
# O(n) space -> using set data structure to track seen numbers
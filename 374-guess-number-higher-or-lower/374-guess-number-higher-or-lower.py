# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n 
        
        while left <= right:
            middle = left + (right - left) // 2
            attempt = guess(middle)

            # target < guess
            if (attempt == -1):
                right = middle - 1
            elif (attempt == 1):
                left = middle + 1
            else:
                return middle
        return -1
            
            
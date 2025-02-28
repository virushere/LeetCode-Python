class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:  # Run the loop while n is not 0
            count += n & 1  # Add 1 if the last bit of n is 1
            n >>= 1  # Right shift n by 1 (remove last bit)
        return count
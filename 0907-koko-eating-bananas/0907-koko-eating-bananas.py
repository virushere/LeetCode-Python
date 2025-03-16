class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        1. Koko eats at a rate of k bananas per hour
        2. If a pile has fewer than k bananas, Koko eats the entire pile in one hour and 
        doesn't eat more during that hour
        3. Koko must finish all bananas within h hours
        4. We need to find the minimum value of k that allows this
        """

        # step 1 find min and max.
        minbound = 1
        maxbound = max(piles)
        while minbound < maxbound:
            mid = (minbound + maxbound)//2
            hours = 0
            # the main logic is below,
            # here we check if we can finish the current i in the array that is pile in specific time ? if yes then we go ahead
            for pile in piles:
                hours += pile // mid
                if pile % mid != 0:
                    hours += 1 # else if we have banana left in the pile after dividing with mid then we add an extra hour to finish the banana
            if hours <= h:
                maxbound = mid
            else:
                minbound = mid + 1
        return minbound
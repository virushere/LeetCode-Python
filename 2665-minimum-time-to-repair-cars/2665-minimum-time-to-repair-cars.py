class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        First we will identify the type of problem,
        To find min or max is generally Binary search type problem.

        In such problems we will find lower and higher bounds.
        lower bound in this case should be,
        Lowerbound = r * n**2 = 1 * 1**2 = 1 // 1 <= ranks[i] <= 100
        Higherbound = r * n**2 = 100 * (10)**6 = 10^14  // 1 <= cars <= 10^6
        """

        lowerbound = 1 # left point
        higherbound = (10)**14 # right point

        while(lowerbound < higherbound):
            mid_point = lowerbound + (higherbound - lowerbound) // 2  
            # This formula is to find average, we can also use mid = (higherbound + lowerbound) // 2
            # But with very large values the value might overflow.
            repaired_cars = 0
            # Now we will, calculate how many cars can be repaired in 'mid' time
            for rank in ranks:
                """
                given time t = r * n**2 
                i.e n**2 = t/r
                n = sqrt(t/r) (In our case t = mid time)
                """
                repaired_cars = repaired_cars + int((mid_point / rank) ** 0.5)  # sqrt(mid/rank)
            if repaired_cars >= cars:
                higherbound = mid_point  # Try to find a smaller time
            else:
                lowerbound = mid_point + 1 # Need more time
        return lowerbound
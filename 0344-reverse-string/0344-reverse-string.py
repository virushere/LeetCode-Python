class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Solution 1 
        # Time: O(n), Space: O(1)
        l = 0
        r = len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l,r = l+1, r-1
"""
We will look at how the code executes relative to the size of the input list `s`.

### **Time Complexity: **

**Calculation:**

1. **Identify the Loop:** The core logic is inside the `while l < r:` loop.
2. **Count Iterations:** In each iteration, `l` increases by 1 and `r` decreases by 1. They start at opposite ends ( and ) and move toward the center.
3. **Total Operations:** Since they move closer by 2 steps per iteration, they will meet after roughly  iterations.
4. **Big-O Simplification:** In Big-O notation, we drop constants like . So,  simplifies to ****.

**Explanation:** The code touches every element exactly once (or twice if you count the swap as touching both), making the time proportional to the number of characters in the list.

### **Space Complexity: **

**Calculation:**

1. **Identify Variables:** You are only using two integer variables, `l` and `r`, to keep track of indices.
2. **Check for Extra Storage:** You are modifying the list `s` "in-place" (meaning you are changing the original list directly rather than creating a new reversed copy). You are not using any extra arrays, stacks, or recursion.
3. **Result:** Since the amount of extra memory used does not grow as the input string gets longer, it is **Constant Space** or ****.

**Summary Table:**

| Metric | Complexity | Reason |
| --- | --- | --- |
| **Time** | $O(n)$ | The loop runs  times, which scales linearly with input size. |
| **Space** | $O(1)$ | No new data structures are created; memory usage is constant. |

"""

        # Solution 2 --> Using Stack
        # Time: O(n), Space: O(n)
        # class Solution:
        #     def reverseString(self, s: List[str]) -> None:
        #         """
        #         Do not return anything, modify s in-place instead.
        #         """
        #         # Time: O(n), Space: O(n)
        #         stack = []
        #         for c in s:
        #             stack.append(c)
        #         i = 0
        #         while stack:
        #             s[i] = stack.pop()
        #             i += 1

        # Solution 3 --> Using Recurssion
        # class Solution:
        #     def reverseString(self, s: List[str]) -> None:
        #         """
        #         Do not return anything, modify s in-place instead.
        #         """
        #         # Time: O(n)
        #         # Space: O(n) due to recursion stack
        #         def reverse(l,r):
        #             if l < r:
        #                 s[l], s[r] = s[r], s[l]
        #                 reverse(l+1,r-1)
        #         reverse(0, len(s)-1)
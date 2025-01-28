# class Solution:
#     def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Create dictionary to store height at each point
        # myDict = {}
        # result = []
        
        # # Process each building
        # for x1, x2, h in buildings:
        #     # Update heights for each x-coordinate
        #     for x in range(x1, x2):
        #         if x not in myDict:
        #             myDict[x] = h
        #         else:
        #             myDict[x] = max(myDict[x], h)
        
        # if not myDict:
        #     return []
        
        # taller_x = min(myDict.keys()) - 1
        # prev_height = 0
        
        # # Process all points in sorted order
        # for x in sorted(myDict.keys()):
        #     curr_height = myDict[x]
            
        #     # Add point only when height changes
        #     if curr_height != prev_height:
        #         if x > taller_x + 1 and prev_height != 0:
        #             result.append([taller_x + 1, 0])
        #         result.append([x, curr_height])
        #         prev_height = curr_height
        #     taller_x = x
        
        # # Add final point where height returns to 0
        # if taller_x < max(myDict.keys()):
        #     result.append([max(myDict.keys()) + 1, 0])
        # else:
        #     result.append([taller_x + 1, 0])
        
        # # Remove redundant points
        # final_result = []
        # for i in range(len(result)):
        #     if i == 0 or result[i][1] != result[i-1][1]:
        #         final_result.append(result[i])
        
        # return final_result
from typing import List
import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Convert buildings to events
        events = []
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start event
            events.append((right, 0, 0))           # End event
        
        # Sort events by position
        events.sort()
        
        result = []
        heap = [(0, float('inf'))]  # (height, right_endpoint)
        
        for pos, height, right in events:
            # Remove buildings that have ended
            while heap[0][1] <= pos:
                heapq.heappop(heap)
            
            # Add new building
            if height < 0:  # Start of building
                heapq.heappush(heap, (height, right))
            
            # Check if max height changed
            curr_max_height = -heap[0][0]  # Negative because of max heap
            if not result or result[-1][1] != curr_max_height:
                result.append([pos, curr_max_height])
        
        return result
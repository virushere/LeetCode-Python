## Simplified solution
# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         # Check if rectangles overlap by verifying:
#         # x-axis overlap and y-axis overlap
#         return (rec1[0] < rec2[2] and        # rec1 left < rec2 right
#                 rec2[0] < rec1[2] and        # rec2 left < rec1 right
#                 rec1[1] < rec2[3] and        # rec1 bottom < rec2 top
#                 rec2[1] < rec1[3])           # rec2 bottom < rec1 top
## Below is ideal solution
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or    # left edge of rec2 is right of rec1
                   rec1[3] <= rec2[1] or     # bottom edge of rec2 is above rec1
                   rec1[0] >= rec2[2] or     # right edge of rec2 is left of rec1
                   rec1[1] >= rec2[3])       # top edge of rec2 is below rec1

class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=46341
        while left<=right:
            mid=left+(right-left)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid+1
            else:
                right=mid-1
        return left-1

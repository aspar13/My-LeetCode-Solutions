class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr = nums[::]
        arr.sort()

        left = 0
        right = len(arr)-1

        while left < right:

            if arr[left] + arr[right] == target:
                return [nums.index(arr[left]), len(arr) - nums[::-1].index(arr[right])-1]
            elif arr[left] + arr[right] < target:
                left += 1
            else:
                right -= 1
        
        return []
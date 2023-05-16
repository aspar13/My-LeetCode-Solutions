class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
		
		arr = nums[::]
		arr.sort()

        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                return arr[i]
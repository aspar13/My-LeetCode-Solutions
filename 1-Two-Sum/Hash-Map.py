class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        for i,num in enumerate(nums):
            if target - num in visited:
                return[visited[target-num], i]
            else:
                visited[num] =  i

        # for num in nums:
        #     if target - num in visited:
        #         return[visited[target-num], len(nums)-nums[::-1].index(num) -1]
        #     else:
        #         visited[num] = nums.index(num)


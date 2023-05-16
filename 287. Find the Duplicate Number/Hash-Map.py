class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        visited = {}

        for element in nums:
            if visited.get(element):
                return element
            else:
                visited[element] = True 
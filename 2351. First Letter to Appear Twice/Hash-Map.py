class Solution:
    def repeatedCharacter(self, s: str) -> str:

        visited = {}

        for ch in s:
            if visited.get(ch):
                return ch
            else:
                visited[ch] = True
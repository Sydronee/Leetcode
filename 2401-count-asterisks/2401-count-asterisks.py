class Solution:
    def countAsterisks(self, s: str) -> int:
        asterisk_count = 0
        pipe_count = 0
        for char in s:
            if char == '|':
                pipe_count += 1
            if pipe_count % 2 == 0:
                if char == '*':
                    asterisk_count += 1
                    
        return asterisk_count
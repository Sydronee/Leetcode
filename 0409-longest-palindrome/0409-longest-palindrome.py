class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequency = Counter(s).items() 
        count = 0
        odd_found = False

        for char, freq in frequency:
            if freq % 2 == 0:
                count += freq
            else:
                if not odd_found:
                    count += freq
                    odd_found = True
                else:
                    count += freq - 1
        
        return count

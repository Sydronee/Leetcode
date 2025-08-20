class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
            
        f = [0] + flowerbed + [0]
        count = 0
        
        for i in range(1, len(f) - 1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                count += 1
                
                if count >= n:
                    return True
        
        return count >= n
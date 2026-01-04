class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for num in nums:
            curr_sum = 0
            count = 0
            
            for i in range(1, int(sqrt(num)) + 1):
                if num % i == 0:
                    if i * i == num:
                        count += 1
                        curr_sum += i
                    else:
                        count += 2
                        curr_sum += i + (num // i)
                
                if count > 4:
                    break
            
            if count == 4:
                total += curr_sum

        return total
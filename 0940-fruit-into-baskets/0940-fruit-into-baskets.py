class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits=0
        left=0
        hashMap={}

        for right in range(len(fruits)):
            fruit=fruits[right]
            hashMap[fruit] = hashMap.get(fruit, 0) + 1

            while len(hashMap)>2:
                leftFruit = fruits[left]
                hashMap[leftFruit]-=1
                
                if hashMap[leftFruit]==0:
                    del hashMap[leftFruit]
                
                left+=1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits
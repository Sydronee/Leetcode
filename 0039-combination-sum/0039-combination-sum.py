class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        res=[]
        
        def combiRec(visited, start, currSum):   
            if currSum==target:
                res.append(list(visited))
                return

            if currSum>target:
                return

            for i in range(start,n):
                visited.append(candidates[i])
                combiRec(visited,i,currSum+candidates[i])
                visited.pop()

        combiRec([],0,0)
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
    
        def backtrack(current_string, open_count, closed_count):
            if len(current_string) == 2 * n:
                result.append(current_string)
                return

            if open_count < n:
                backtrack(current_string + "(", open_count + 1, closed_count)
                
            if closed_count < open_count:
                backtrack(current_string + ")", open_count, closed_count + 1)
                
        backtrack("", 0, 0)
        return result
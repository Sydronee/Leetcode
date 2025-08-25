class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        result = {item[0]: item[1] for item in paths}

        initial=result[paths[0][0]]

        while initial in result.keys():
            initial=result[initial]
        return initial
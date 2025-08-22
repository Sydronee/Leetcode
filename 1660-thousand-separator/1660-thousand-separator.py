class Solution:
    def thousandSeparator(self, n: int) -> str:
        formatted_string = f'{n:,}'
        return formatted_string.replace(',','.')
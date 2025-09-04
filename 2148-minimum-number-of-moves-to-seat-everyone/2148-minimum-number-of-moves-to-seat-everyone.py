class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        moves=0
        seats.sort()
        students.sort()
        for i, j in zip(seats,students):
            moves+=abs(i-j)
        return moves
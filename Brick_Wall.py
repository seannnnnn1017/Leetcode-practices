class Solution:
    def leastBricks(self, A=[   [1,2,2,1],
                                [3,1,2],
                                [1,3,2],
                                [2,4],
                                [3,1,2],
                                [1,3,1,1]]) -> int:
        freq = {}
        max_freq = 0
        for row in A:
            position = 0
            for brick in row[:-1]:
                position += brick
                freq[position] = freq.get(position, 0) + 1
                max_freq = max(max_freq, freq[position])
                print(freq)
        return len(A) - max_freq

Solution.leastBricks(None)
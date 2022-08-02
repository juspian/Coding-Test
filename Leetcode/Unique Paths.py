class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res=1
        for i in range(max(m,n), m+n-1):
            res*=i
        for i in range(1,min(m,n)):
            res//=i
        return res
    
    # Recursion: 비효율적인 경우가 많음
    #-> DP나 iteration
    # iteration: 포인터를 사용하는 방식
    # DP: 작은 문제를 저장하는 방식
    
    # DP 풀이
    class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for _ in range(m)]  # m*n행렬을 생성하고 1을 넣음

        for x in range(1, m):
            for y in range(1, n):
                paths[x][y] = paths[x - 1][y] + paths[x][y - 1]

        return paths[m - 1][n - 1]

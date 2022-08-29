class Solution:
    def generateMatrix(self, n: int) :
        t,b,l,r = 0, n, 0, n
        result = [[0 for _ in range(n)] for _ in range(n)]
        nums , tar = 1, n*n
        while nums <= tar:
            for i in range(l,r):
                result[t][i] = nums
                nums += 1
            t += 1
            for i in range(t,b):
                result[i][r-1] = nums
                nums += 1
            r -= 1
            for k in range(r-1,l-1,-1):
                result[b-1][k] = nums
                nums += 1
            b -= 1
            for i in range(b-1,t-1,-1):
                result[i][l] = nums
                nums += 1
            l += 1
        return result

a = Solution()
print(a.generateMatrix(3))
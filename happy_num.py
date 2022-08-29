class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = set()
        def cal_happy(num):
            res = 0
            while num:
                res += (num%10) * (num%10)
                num //= 10
            return res

        while True:
            n = cal_happy(n)
            if n == 1: return True
            if n in tmp: return False
            else:
                tmp.add(n)

a = Solution()
print(a.isHappy(19))

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def minSubArrayLen(self, target, nums) :
        # if not nums: return 0
        # n = len(nums)
        # length, result= 0,n+1
        # for i in range(n):
        #     sums = 0
        #     for j in range(i,n):
        #         sums += nums[j]
        #         if sums >= target:
        #             result = min(result , j-i+1)
        #             break
        #     return 0 if result == n+1 else result
        if not nums: return 0
        n = len(nums)
        ans = n + 1
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    ans = min(ans, j - i + 1)
                    break

        return 0 if ans == n + 1 else ans
# Press the green button in the gutter to run the script.

a = Solution()
print(a.minSubArrayLen(7,[2,3,1,2,4,3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

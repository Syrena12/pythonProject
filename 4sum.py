class Solution:
    def fourSum(self, nums, target) :
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j+1
                right = n-1
                print(i,j,left,right)
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target :
                        left += 1
                    else:
                        res.append([nums[i] , nums[j] , nums[left] , nums[right]])
                        if left < right and nums[left] == nums[left+1]:
                            left += 1
                        if left < right and nums[right] == nums[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res

a = Solution()
print(a.fourSum([-9,-2,-2,-7,5,5,-2,-9,5],-13))
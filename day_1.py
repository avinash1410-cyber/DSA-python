class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        n = len(nums)

        for f in range(n - 2):
            if f > 0 and nums[f] == nums[f - 1]:
                continue
            req = -nums[f]
            l = f + 1
            r = n - 1
            while l < r:
                if nums[l] + nums[r] == req:
                    ans.append([nums[f], nums[l], nums[r]])
                    l=l+1
                    while l < r and nums[l-1] == nums[l + 1]:
                        l += 1
                    r=r-1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < req:
                    l += 1
                else:
                    r -= 1
        return ans


    def ksum(self,nums,k,target,i):
        ans=[]
        if k==2:
            l=i
            r=len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append(nums[l], nums[r])
                    l=l+1
                    while l < r and nums[l-1] == nums[l + 1]:
                        l += 1
                    r=r-1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1


        for j in range(i,len(nums)-1):
            if j >i and nums[j]==nums[j-1]:
                continue
            new_target=target-nums[j]
            n_ans=self.ksum(nums,k-1,new_target,i+1)
            for l in n_ans:
                ans.append([nums[i]]+l)
        return ans
        
    def fourSum(self, nums, target):
        sorted(nums)
        return self.ksum(nums,4,target,0)
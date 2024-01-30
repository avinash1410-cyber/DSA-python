def threeSum(self, nums):
        nums.sort() # We sort nums first to more easily find duplicate numbers
        triplets = [] # We will store all the valid triplets in here
        
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue # Skip duplicates
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                if curSum == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1;
                    
                    # Skip all duplicates on left side
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                    
                    # Skip all duplicates on right side
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                elif curSum < 0:
                    left += 1 # Our sum is too small, so we try to increase the sum
                else:
                    right -= 1 # Our sum is too big, so we try to decrease the sum
        return triplets


#################################################################3




def ksum(k, nums, l, r, target):
        ans = []

        if k == 2:
            while l < r:
                if nums[l] + nums[r] == target:
                    ans.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(l, r + 1):
                if i > l and nums[i] == nums[i - 1]:
                    continue
                subtarget = target - nums[i]
                sub_ans = ksum(k - 1, nums, i + 1, r, subtarget)
                for sa in sub_ans:
                    ans.append([nums[i]] + sa)

        return ans





def ksum(k,nums,l,r,target):
    ans=[]
    if k==2:
        while l<r:
            if nums[l]+nums[r]>target:
                r=r-1
                while nums[r]==nums[r-1]:
                    r=r-1
            elif nums[l]+nums[r]<target:
                l=l+1
                while nums[l]==nums[l+1]:
                    l=l+1
            else:
                ans.append(l,r)
        return ans
    
    st=1
    while nums[st]==nums[st-1]:
        st=st+1
    nums=nums[1:-1]
    target=-(target+nums[0])
    pr_ans=ksum(k-1,nums,0,len(nums)-1,target)
    ans=[nums[0]].append(pr_ans)
    return ans





342+465=807

[2,4,3,5,7]
[5,6,4]
[7,0,8,5,7]
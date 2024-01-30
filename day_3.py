class Solution(object):
    def get_len(s,l,r):
        ans=0
        while s[l]==s[r]:
            ans=r-l
            l=l-1
            r=r+1
        return ans
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        r=0
        ans=0
        while r<len(s):
            a1=self.get_len(s,r,r)
            a2=0
            if r+1<len(s):
                a2=self.get_len(s,r,r+1)
            ans=max(ans,max(a1,a2))
            r=r+1


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        
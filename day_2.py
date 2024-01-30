class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        l=0
        r=0
        if len(s)<=1:
            return len(s)
        S=set()
        while r<len(s):
            if s[r] not in S:
                S.add(s[r])
                r=r+1
                ans=max(ans,r-l)
            else:
                # S.remove(s[l])
                while s[l]==s[r]:
                    l=l+1
                L=l+1
        return ans
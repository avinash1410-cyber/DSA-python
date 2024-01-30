import collections

def levelorder(root):
    q=collections.dequeue()
    q.append(root)
    ans=[]
    while q:
        cl=[]
        l=len(q)
        while l:
            te=q.remove()
            cl.append(te)
            if te.left:
                q.append(te.left)
            if te.right:
                q.append(te.right)
            l=l-1
    return ans


def pathsum(root):
    ans=0
    if root is None:
        return 0
    l=pathsum(root.left)
    r=pathsum(root.right)
    ans=max(root.val+l+r,ans)
    return max(max(root.val+l,root.val+r),root.val)

def right_view(root):
    ans=[]
    fa=[]
    if root is None:
        return ans
    q=collections.dequeue()
    q.append(root)
    while q:
        cl=[]
        l=len(q)
        f=False
        while l:
            if f==False:
                fa.append(te.val)
                f=True
            te=q.remove()
            cl.append(te)
            if te.right:
                q.append(te.right)
            if te.left:
                q.append(te.left)
            l=l-1
    return ans


def right_view_dfs(root,cl,hl,ans):
    if root is None:
        return
    if root.right and cl>hl:
        ans.append(root.right.val)
    if root.right is None and root.left and cl>hl:
        ans.append(root.left.val)
    hl=max(cl,hl)
    right_view_dfs(root.left,cl+1,hl,ans)
    return ans
        

defboat to save ppl(ppl):
    sort(ppl)
    l=0
    r=len(ppl)-1
    while l<r:
        if ppl[r]+ppl[l]<=limit:
            ans=ans+1
            l=l+1
            r=r-1
        else:
            ans=ans+1
            r=r-1
        return ans


def matrix_cut(matrix):
    
    fr=matrix[0]
    l=0
    for cd in fr:
        l=l+cd
    
    D={i:0,for i in range(l)}

    r1=0
    r2=r1+1


    while r2<=len(matrix):
        s1=set()
        s2=set()
        v1=matrix[r1]
        v2=matrix[r2]
        dc=0
        for v in v1:
            dc=dc+v
            s1.add(dc)
        dc=0
        for v in v2:
            dc=dc+v
            s2.add(dc)
        for s in s1:
            if s not in s2:
                D{s}=D{s}
        r1=r1+1
        r2=r2+1
    
    ans=9999999999
    for k in D.keys():
        ans=min(ans,D[k])
    return ans
        
        
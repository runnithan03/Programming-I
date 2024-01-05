def lmax(lst):
    i=0
    val=0
    n=len(lst)
    while i<=n-1:
        x=lst[i]
        if x>val:
            val=x
            i=i+1
        else:
            i=i+1
    return val

print(lmax([5,8,348759837495873498759834753,8975987439854]))
        
    
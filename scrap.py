t = int(input())
for _ in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().split()))
    sm = sum(arr)
    pref = [0]
    num = 0
    for n in arr:
        num+=n
        pref.append(num)
    for _ in range(q):
        l,r,k = map(int,input().split())
        temp = pref[r]-pref[l-1]
        if (sm-temp+(r-l+1)*k)%2:
            print('yes')
        else:
            print('no')
    
    
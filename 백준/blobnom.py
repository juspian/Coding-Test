n= int(input())
blob= list(map(int, input().split()))
height=[]

if n<=2:
    print(max(blob))
else:
    for i in range(1, n-1):
        ans= blob[i]+min(blob[i-1],blob[i+1])
        height.append(ans)
    height.append(max(blob[0],blob[-1]))
    print(max(height))

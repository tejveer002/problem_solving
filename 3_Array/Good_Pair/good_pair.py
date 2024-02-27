def solve(arr):
    count = 0
    for x in range(len(arr)):
        for y in range(x+1,len(arr)):
            if arr[x] +arr[y] == k and x != y:
                count +=1
    return 0

arr = list(map(int,input("").strip().split()))
k = int(input(""))

res = solve(arr)
print(res)
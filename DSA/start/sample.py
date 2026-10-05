def solve( b: int, arr: list[int]) -> int:
    # code here
    n = len(arr)
    for x in arr:
        if x==b:
            b = b*2
    return b
b = 2
arr = [1, 2, 3, 4, 8]
print(solve(b,arr))
        
                

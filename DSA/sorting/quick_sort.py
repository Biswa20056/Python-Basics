'''def quick_sort(arr):
    if len(arr)<=1:
        return arr
    n = len(arr)
    pivot = arr[n//2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    mid = [x for x in arr if x==pivot]
    return quick_sort(left) + mid + quick_sort(right)
arr = [4,1,7,6,3,2,8]
print(quick_sort(arr))'''
arr = [4,1,7,6,3,2,8]
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j
def quicksort(arr,low,high):
    if low<high:
        p_idx = partition(arr,low,high)
        quicksort(arr,low,p_idx-1)
        quicksort(arr,p_idx+1,high)
arr = [4,1,7,6,3,2,8]
n = len(arr)
low = 0
high = n-1
quicksort(arr,low,high)
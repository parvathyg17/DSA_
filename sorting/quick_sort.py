def partition(arr,low,high):
    pivot=low
    i=low+1
    j=high
    while i<=j:
        while i<=j and arr[i]<=arr[pivot]:
            i+=1
        while i<=j and arr[j]>=arr[pivot]:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[pivot],arr[j]=arr[j],arr[pivot]
    return j
def quick_sort(arr,low,high):
    if low<high:
        pivot_index=partition(arr,low,high)
        quick_sort(arr,low,pivot_index-1)
        quick_sort(arr,pivot_index+1,high)

arr=[6,3,2,8,1,7,4]
quick_sort(arr,0,len(arr)-1)
print(arr)

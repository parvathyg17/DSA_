arr=[6,2,8,3]
def bubble_sort(arr):
    n=len(arr)
    for i in range(len(arr)):
        for j in range(n-1-i):
            if arr[j]>=arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
bubble_sort(arr)
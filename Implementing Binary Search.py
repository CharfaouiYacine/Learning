def binary_search(arr,target):
    beg = 0
    end = len(arr)-1
    while beg <= end:
        mid = (beg + end) //2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            beg = mid+1
        else:
            end = mid-1
    return None

llist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary_search(llist,11)) # Will return index 10
print(binary_search(llist,21)) # Will return None
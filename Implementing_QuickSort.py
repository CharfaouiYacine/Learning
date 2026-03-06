def quicksort(arr):
    if len(arr)<2:  # this is the base case if the array has one element or zero elements just return the list
        return arr
    else:
        pivot = arr[0] # we take the first element of the array as the pivot
        less = []
        greater = []
        for i in arr[1:]:  # check from the second to the last elements
            if i<=pivot:
                less.append(i) # is this array we add all the elements that are less or equal to the pivot
            elif i>pivot:
                greater.append(i) # in this array we add all the elements that are greater than the pivot
    return quicksort(less) + [pivot] + quicksort(greater) # here we call the function  the two sub arrays and merge them into one array

mylist = quicksort([20,20,-4,100,2,55,4,1,3,-20])
print(mylist)
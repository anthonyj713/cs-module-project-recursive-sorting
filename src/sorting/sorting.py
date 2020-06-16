# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    indexA = 0
    indexB = 0
    merged_arr = []

    while indexA < len(arrA) and indexB < len(arrB):
        if arrA[indexA] < arrB[indexB]:
            merged_arr.append(arrA[indexA])
            indexA += 1
        else:
            merged_arr.append(arrB[indexB])
            indexB += 1

    merged_arr += arrA[indexA:]
    merged_arr += arrB[indexB:]

    # Your code here

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr
    
    half = len(arr) // 2
    arrA = merge_sort(arr[:half])
    arrB = merge_sort(arr[half:])

    return merge(arrA, arrB)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass



def merge_sort_in_place(arr, l, r):
    # Your code here
    pass


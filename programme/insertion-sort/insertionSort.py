# Write a program for Insertion Sort in Python
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__=='__main__':
    arr = [14, 33, 27, 35 ,10]
    print("Input: ", arr)
    print("Output: ", insertionSort(arr))

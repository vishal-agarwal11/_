def mergeSort(arr):
    if len(arr) > 1:
        mid = int(len(arr)/2)
        leftarr = arr[0:mid]
        rightarr = arr[mid:]

        print(f"leftarr = {leftarr}, rightarr = {rightarr}")
        mergeSort(leftarr)
        mergeSort(rightarr)

        i = 0
        j = 0
        k = 0

        print(f"Assembling - leftarr = {leftarr}, rightarr = {rightarr}")
        while(i < len(leftarr) and j < len(rightarr)):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = rightarr[j]
                j = j + 1
                k = k + 1
        print(f"FW ##### arr = {arr}")

        while(i < len(leftarr)):
            arr[k] = leftarr[i]
            i = i + 1
            k = k + 1
        print(f"SW ##### arr = {arr}")
            
        while(j < len(rightarr)):
            arr[k] = rightarr[j]
            j = j + 1
            k = k + 1
        print(f"TW ##### arr = {arr}")

        return arr


print(mergeSort([2,6,4,9,1,5]))
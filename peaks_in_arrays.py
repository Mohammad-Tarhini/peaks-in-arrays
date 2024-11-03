def peaks_of(arr):
    peaks_indices=[]
    if arr[0]>arr[1]:
        peaks_indices.append(0)
    for i in range(1,len(arr)-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            peaks_indices.append(i)
    if arr[len(arr)]>arr[len(arr)-1]:
        peaks_indices.append(len(arr))
    return peaks_indices


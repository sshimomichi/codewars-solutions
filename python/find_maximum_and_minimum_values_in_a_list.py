def minimum(arr):
    # Assign the 0nth value in array to mi
    mi = arr[0]
    for i in arr:
        if i < mi:
            mi = i
    return mi

def maximum(arr):
    # Assign the 0nth value in array to ma
    ma = arr[0]
    for i in arr:
        if i > ma:
            ma = i
    return ma

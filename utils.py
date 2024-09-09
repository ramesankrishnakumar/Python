def find_max(arr):
    max_element = arr[0]
    for i in arr:
        if i > max_element:
            max_element = i
    return max_element
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return iterations, arr[mid]
        
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    if left < len(arr):
        return iterations, arr[left]
    else:
        return iterations, None


arr = [0.1, 0.4, 0.7, 1.2, 1.5, 2.3, 3.0, 4.6]
target = 1.5

iterations, upper_bound = binary_search(arr, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")

target = 2.5
iterations, upper_bound = binary_search(arr, target)
print(f"Ітерацій: {iterations}, Верхня межа: {upper_bound}")

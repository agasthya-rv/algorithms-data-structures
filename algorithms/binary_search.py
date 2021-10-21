# Binary search -> Expects sorted array/ list
# Time Complexity -> O(logn)

def binary_search(array, key):
    list_len = len(array) if array else 0
    low = 0
    high = list_len - 1
    
    if list_len == 0:
        return None
    
    while low <= high:
        mid = (low + high) // 2
        val = array[mid]
        if key == val:
            return mid
        elif key < val:
            high = mid - 1
        else:
            low = mid + 1


# Unit Tests
array1 = [2, 9, 45, 67, 99, 112, 175, 189]
array2 = [21, 93, 145, 627, 999, 1112, 1275, 10089, 12345]

print("Location of number 88 in Array1:",binary_search(array1,88))
print("Location of number 112 in Array1:",binary_search(array1,112))
print("Location of number 93 in Array2:",binary_search(array2,93))
print("Location of number 1234 in Array2:",binary_search(array2,1234))

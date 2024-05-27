def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement

def main():
    # Prompt user to input an array of integers
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    
    print("Array:", arr)
    
    # Sort the array using quick sort algorithm
    sorted_arr = quick_sort(arr)
    
    print("Sorted Array using Quick Sort:", sorted_arr)
    
    # Allow user to specify a target element to search for
    target = int(input("Enter the element to search for: "))
    
    # If target element is found, prompt user to input a replacement element
    if target in sorted_arr:
        replacement = int(input("Enter the replacement element: "))
        # Replace all occurrences of target element with replacement element
        replace_elements(sorted_arr, target, replacement)
        print(f"Modified Array after replacing {target} with {replacement}: {sorted_arr}")
    else:
        print("Target element not found in the array.")

if __name__ == "__main__":
    print("Array Sorting and Element Replacement")
    main()

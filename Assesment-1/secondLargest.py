nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest = second_largest = float('-inf')
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
if second_largest == float('-inf'):
    print("No second largest element exists.")
else:
    print("The second largest element is:", second_largest)
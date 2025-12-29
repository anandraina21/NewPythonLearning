nums = [0, 1, 2, 3, 4, 5]
nums.append(6)
print("Print nums array:", nums, "Type:", type(nums), sep="\n")

print("\nElement at nums[0]:", nums[0])
print("Last element in array:", nums[-1])
print("Element at nums[2]:", nums[2])

print("\nFor loop to print nums array:")
for n in nums:
    print(n, end=" ")

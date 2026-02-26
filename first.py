ans  = []
for i in range(5):
    nums = int(input(f"enter a number{i+1}:"))
    ans.append(nums)

print("the list is", ans)
ans.sort()
print("the sorted list is:", ans)
out = sum(ans)
print("the sum of the list is:", out)
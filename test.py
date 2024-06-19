def two_sum(nums, target):
  num_indices = {}
  for i, num in enumerate(nums):
      complement = target - num
      if complement in num_indices:
          return [num_indices[complement], i]
      num_indices[num] = i

# Пример использования
nums = [2, 11, 7, 15]
target = 9
result = two_sum(nums, target)
print(result)
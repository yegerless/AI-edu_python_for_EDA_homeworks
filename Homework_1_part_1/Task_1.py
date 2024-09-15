a, b, c = int(input()), int(input()), int(input())
nums = list(map(int, input().split(', ')))

[print(num) for num in nums if num >= a and num <= b and num % c == 0]
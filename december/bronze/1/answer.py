from collections import defaultdict

n = int(input()) # First line is how many numbers there are
numbers = input().strip().split() # Second line is the numbers
assert len(numbers) == n # Make sure the length of the list is n
numbers = [int(i) for i in numbers] # Convert the numbers to integers
counts = defaultdict(int)
prices = defaultdict(list)
for num in numbers:
    counts[num] += 1
current_excluded = 0
for price, num_excluded in sorted(counts.items(), key=lambda item: item[0]):
    money_made = (n - current_excluded) * price
    prices[money_made].append(price)
    current_excluded += num_excluded

max_made = sorted(prices.keys())[-1]
prices[max_made].sort()
print(f"{max_made} {prices[max_made][0]}")
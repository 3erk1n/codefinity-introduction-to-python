prices = [29.99, 45.50, 12.75, 38.20]

for a in range(len(prices)):
    if a == 0: 
        discount = 0.10 
    elif a == 1:
        discount = 0.20
    elif a == 2:
        discount = 0.15
    elif a == 3:
        discount = 0.05
    prices[a] -= prices[a] * discount

print(f"Updated price for item {a}: ${prices[a]:.2f}")

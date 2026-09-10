#### MULTIPLICATION TABLE ####

print("=" * 40)
print("       MULTIPLICATION TABLE")
print("=" * 40)

num = int(input("Enter a number: "))

# Choose how many multiples to print
limit = int(input("Enter the limit: "))

print("\n" + "-" * 40)
print(f"        TABLE OF {num}")
print("-" * 40)

total = 0

for i in range(1, limit + 1):

    result = num * i
    total += result

    print(f"{num} x {i} = {result}")

print("-" * 40)
print(f"Total of all multiples: {total}")
print("-" * 40)
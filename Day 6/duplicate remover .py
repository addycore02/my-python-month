#### DUPLICATE REMOVER ####

print(" DUPLICATE REMOVER ")

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(" Original List :", numbers)
print(" List Without Duplicates :", unique_numbers)

#### OUTPUT #####

DUPLICATE REMOVER
Original List : [10, 20, 10, 30, 20, 40, 30, 50]
List Without Duplicates : [10, 20, 30, 40, 50]
#### COMMON ELEMENTS FINDER ####

print(" COMMON ELEMENTS FINDER ")

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common_elements = []

for number in list1:
    if number in list2:
        common_elements.append(number)

print(" First List :", list1)
print(" Second List :", list2)
print(" Common Elements :", common_elements)

#### OUTPUT ####

COMMON ELEMENTS FINDER
First List : [10, 20, 30, 40, 50]
Second List : [30, 40, 50, 60, 70]
Common Elements : [30, 40, 50]
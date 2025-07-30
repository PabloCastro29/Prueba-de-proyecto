import random 

Aleatories_numbers = [random.randint(1, 100) for cantidad in range(20)]
print("Lista hecha:", Aleatories_numbers)
print("Miltiplos de 3:")

for element in Aleatories_numbers:
    if element % 3 ==0:
        print(element, end =",")
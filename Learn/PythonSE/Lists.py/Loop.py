frutas = ["Manzana", "guayaba", "naranja", "melon", "plátano"]

# For
for i in range(len(frutas)):
    print(frutas[i])

# For-each
for f in frutas:
    print(f)

# While
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# Looping using List Comprehension
[print(f) for f in frutas]
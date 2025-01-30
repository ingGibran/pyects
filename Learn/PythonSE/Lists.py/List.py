# Introduction
miLista = [1, 2, 3]
print(miLista)

for i in miLista:
    print(i)
    
print(type(miLista))
print(len(miLista))

# Access
frutas = list(("manzana", "naranja", "sandia"))
print(frutas[1])
print(frutas[-2])
print(frutas[:2])
print("manzana" in frutas)

# Change List Items
nombres = ["Tomas", "Juan", "Roberto", "Manuel", "Tomas"]
print(nombres)

nombres[len(nombres)-1] = "Ricardo"
print(nombres)

nombres[0:2] = ["Josue", "Morales"]
print(nombres)

# Insert (index, item)
nums = [1, 2, 3, 5, 6]
print(nums)

nums.insert(3, 4)
print(nums)

# Add (Tail)
mult_dos = [2, 4, 6, 8]
for i in range(4):
    elemento = (i+4) * 2
    mult_dos.append(elemento)
print(mult_dos)

# Remove
verduras = ["brocoli", "lechuga", "zanahoria"]
print(verduras)
verduras.remove("brocoli")
print(verduras)

# Pop
verduras.pop(0)
print(verduras)

# Pop Last item
verduras.pop()
print(verduras)

# del (eliminar)
postres = ["helado", "chocolate", "dulce"]
print(postres)
"""
del postres
print(postres)
""" # Ya no existe postres

# clear (vaciar)
paises = ["México", "USA", "España", "Japón"]
print(paises)
paises.clear()
print(paises)
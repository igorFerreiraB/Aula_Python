# forma comum
# for item in range(10):
#     lista.append(item*2)

# list comprehensions
lista = [item**2 for item in range(10)]

print (lista)

# list comprehensions também pode conter condicionais para criar listas ou modificar listas existentes

# forma comum
# for item in range(10):
#     if item % 2 == 0:
#         print (item)

# list comprehensions 
result = [item for item in range(20) if item % 2 == 0]

print(result)

square = []
for i in range(1,11):
    square.append(i**2)

square = [i**2 for i in range(1,11)]
print(square)



even_num = [i for i in range(1,11) if i % 2 == 0]
print(even_num)

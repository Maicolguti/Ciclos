n = int(input("Ingrese el valor máximo para la secuencia de Fibonacci: "))
a = 0
b = 1
print("Secuencia de Fibonacci:")
while a <= n:
	print(a, end=" ")
	x = a
	a = b
	b = x + b
print()

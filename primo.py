num = int(input("Ingrese un número para saber si es primo o no: "))  # Solicita un número al usuario

# Un número primo es mayor o igual a 2
if num < 2:
	print(num, " no es primo.")
else:
	es_primo = True  # Suponemos que el número es primo
	# Verificamos si tiene algún divisor entre 2 y la raíz cuadrada de num
	for i in range(2, int(num ** 0.5) + 1):
		if num % i == 0:
			es_primo = False  # Si encontramos un divisor, no es primo
			break
	# Mostramos el resultado
	if es_primo:
		print(num, "es primo.")
	else:
		print(num, "no es primo.")
